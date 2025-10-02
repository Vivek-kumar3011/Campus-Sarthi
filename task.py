# task.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime
import uuid

# CSV file path
TASKS_CSV = "tasks_data.csv"

def initialize_csv():
    """Initialize CSV file with required columns if it doesn't exist"""
    if not os.path.exists(TASKS_CSV):
        df = pd.DataFrame(columns=['task_id', 'student_name', 'description', 'status', 'created_date'])
        df.to_csv(TASKS_CSV, index=False)

def load_tasks():
    """Load all tasks from CSV file"""
    initialize_csv()
    try:
        df = pd.read_csv(TASKS_CSV)
        # Convert to dictionary format: {student_name: [tasks]}
        tasks_dict = {}
        for _, row in df.iterrows():
            student_name = row['student_name']
            if student_name not in tasks_dict:
                tasks_dict[student_name] = []
            
            task = {
                'task_id': row['task_id'],
                'description': row['description'],
                'status': row['status'],
                'created_date': row['created_date'],
                'student': student_name
            }
            tasks_dict[student_name].append(task)
        
        return tasks_dict
    except Exception as e:
        st.error(f"Error loading tasks: {e}")
        return {}

def save_tasks(tasks_dict):
    """Save all tasks to CSV file"""
    try:
        all_tasks = []
        for student_name, tasks in tasks_dict.items():
            for task in tasks:
                all_tasks.append({
                    'task_id': task['task_id'],
                    'student_name': student_name,
                    'description': task['description'],
                    'status': task['status'],
                    'created_date': task['created_date']
                })
        
        df = pd.DataFrame(all_tasks)
        df.to_csv(TASKS_CSV, index=False)
        return True
    except Exception as e:
        st.error(f"Error saving tasks: {e}")
        return False

def get_student_tasks(student_name):
    """Get tasks for a specific student"""
    tasks_dict = load_tasks()
    return tasks_dict.get(student_name, [])

def update_student_tasks(student_name, tasks_list):
    """Update tasks for a specific student"""
    tasks_dict = load_tasks()
    tasks_dict[student_name] = tasks_list
    return save_tasks(tasks_dict)

def delete_student_tasks(student_name):
    """Delete all tasks for a specific student"""
    tasks_dict = load_tasks()
    if student_name in tasks_dict:
        del tasks_dict[student_name]
        return save_tasks(tasks_dict)
    return True

def show_student_dashboard(student_name, student_tasks):
    """Show dashboard for a specific student"""
    
    if not student_tasks:
        st.info("📝 No tasks added yet. Add your first task above!")
        return
    
    # Calculate progress
    total_tasks = len(student_tasks)
    completed_tasks = len([t for t in student_tasks if t['status'] == 'completed'])
    partial_tasks = len([t for t in student_tasks if t['status'] == 'partial'])
    
    # Calculate score (Full=1 point, Partial=0.5 points)
    if total_tasks > 0:
        score = ((completed_tasks * 1.0) + (partial_tasks * 0.5)) / total_tasks * 100
    else:
        score = 0
    
    # Display progress metrics
    st.subheader("📊 Progress Dashboard")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Tasks", total_tasks)
    with col2:
        st.metric("Completed", completed_tasks)
    with col3:
        st.metric("Partial", partial_tasks)
    with col4:
        st.metric("Score", f"{score:.1f}%")
    
    # Display badge
    st.subheader("🏆 Your Badge")
    badge_col1, badge_col2, badge_col3 = st.columns([1, 2, 1])
    
    with badge_col2:
        if score == 100:
            st.success("🎖️ **GOLD BADGE** - Excellent! All tasks fully completed!")
        elif score >= 67:
            st.warning("🥈 **SILVER BADGE** - Great job! Most tasks completed!")
        elif score >= 50:
            st.info("🥉 **BRONZE BADGE** - Good progress! Half tasks completed!")
        else:
            st.error("❌ **No badge yet** - Keep working on your tasks!")
    
    st.markdown("---")
    
    # Task list with actions
    st.subheader("📝 Your Task List")
    for task in student_tasks:
        with st.container():
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            
            with col1:
                # Display task with status indicator
                status_icon = {
                    'completed': '✅',
                    'partial': '🟡', 
                    'pending': '⭕'
                }
                status_text = {
                    'completed': f"~~{task['description']}~~",
                    'partial': f"{task['description']} (Partial)",
                    'pending': task['description']
                }
                st.write(f"{status_icon[task['status']]} {status_text[task['status']]}")
                st.caption(f"Added: {task['created_date']}")
            
            with col2:
                if st.button("✅ Full", key=f"complete_{task['task_id']}", use_container_width=True):
                    task['status'] = 'completed'
                    if update_student_tasks(student_name, student_tasks):
                        st.success("Task marked as completed!")
                        st.rerun()
            
            with col3:
                if st.button("🟡 Partial", key=f"partial_{task['task_id']}", use_container_width=True):
                    task['status'] = 'partial'
                    if update_student_tasks(student_name, student_tasks):
                        st.success("Task marked as partial!")
                        st.rerun()
            
            with col4:
                if st.button("🗑️", key=f"delete_{task['task_id']}", use_container_width=True):
                    # Remove the specific task
                    updated_tasks = [t for t in student_tasks if t['task_id'] != task['task_id']]
                    if update_student_tasks(student_name, updated_tasks):
                        st.success("Task deleted!")
                        st.rerun()
            
            st.markdown("---")
    
    # Progress visualization
    st.subheader("📈 Progress Chart")
    if total_tasks > 0:
        progress_data = {
            'Status': ['Completed', 'Partial', 'Pending'],
            'Count': [completed_tasks, partial_tasks, total_tasks - completed_tasks - partial_tasks]
        }
        progress_df = pd.DataFrame(progress_data)
        st.bar_chart(progress_df.set_index('Status'))
    
    # Reset button
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Reset All My Tasks", use_container_width=True):
            if delete_student_tasks(student_name):
                st.success("All your tasks have been reset!")
                st.rerun()
    
    with col2:
        # Show all students overview (admin view)
        if st.checkbox("👥 Show All Students Overview"):
            show_all_students_overview()

def show_all_students_overview():
    """Show overview of all students' progress"""
    st.subheader("👥 All Students Progress")
    
    tasks_dict = load_tasks()
    if not tasks_dict:
        st.info("No students have added tasks yet.")
        return
    
    overview_data = []
    for student_name, tasks in tasks_dict.items():
        total_tasks = len(tasks)
        completed_tasks = len([t for t in tasks if t['status'] == 'completed'])
        partial_tasks = len([t for t in tasks if t['status'] == 'partial'])
        
        if total_tasks > 0:
            score = ((completed_tasks * 1.0) + (partial_tasks * 0.5)) / total_tasks * 100
        else:
            score = 0
        
        # Determine badge
        if score == 100:
            badge = "🎖️ Gold"
        elif score >= 67:
            badge = "🥈 Silver"
        elif score >= 50:
            badge = "🥉 Bronze"
        else:
            badge = "❌ None"
        
        overview_data.append({
            'Student': student_name,
            'Total Tasks': total_tasks,
            'Completed': completed_tasks,
            'Partial': partial_tasks,
            'Score': f"{score:.1f}%",
            'Badge': badge
        })
    
    overview_df = pd.DataFrame(overview_data)
    st.dataframe(overview_df, use_container_width=True, hide_index=True)

def show():
    """Main Task Manager function"""
    
    st.title("📋 Campus-Sarthi: Task Manager")
    st.markdown("Manage your tasks and earn points with badges!")
    st.markdown("---")
    
    # Student name input
    col1, col2 = st.columns([2, 1])
    with col1:
        student_name = st.text_input("Enter your name:", 
                                   placeholder="Enter your name to track tasks",
                                   key="student_name_input")
    
    if student_name:
        # Load tasks for this student
        student_tasks = get_student_tasks(student_name)
        
        # Add new task
        st.subheader("➕ Add New Task")
        with st.form("add_task_form", clear_on_submit=True):
            task_desc = st.text_input("Task Description:", placeholder="Enter your task here...")
            submitted = st.form_submit_button("Add Task")
            
            if submitted and task_desc:
                new_task = {
                    'task_id': str(uuid.uuid4())[:8],  # Generate unique ID
                    'description': task_desc,
                    'status': 'pending',
                    'created_date': datetime.now().strftime("%Y-%m-%d %H:%M"),
                    'student': student_name
                }
                
                # Add to student's tasks and save
                student_tasks.append(new_task)
                if update_student_tasks(student_name, student_tasks):
                    st.success("✅ Task added successfully!")
                    st.rerun()
                else:
                    st.error("❌ Failed to save task!")
        
        st.markdown("---")
        
        # Show student dashboard
        show_student_dashboard(student_name, student_tasks)
    
    else:
        st.warning("👆 Please enter your name above to start using the Task Manager!")
        
        # Show overview if no student selected
        st.markdown("---")
        show_all_students_overview()