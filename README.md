# toDoList
-----

This is a simple network driven to-do list application that allows users to create, read, update, and delete tasks.  The
application is built using gRPC and Python, it uses mutliple sources for data storage, including a local SQLite database
and a remote PostgreSQL database.

I am planning on adding a feature to organize tasks into projects, and to allow users to share tasks with others.  I am
also adding a feature to allow users to determine the priority of tasks, and to set deadlines for tasks.

## Features
- Create, read, update, and delete tasks
- Store tasks in a local SQLite database
- Store tasks in a remote PostgreSQL database
- Organize tasks into projects (coming soon)
- Share tasks with others (coming soon)
- Set task priority (coming soon)
- Set task deadlines (coming soon)
- Search tasks by title or description
- Filter tasks by status (completed, pending, etc.)
- Sort tasks by priority or deadline
- Export tasks to CSV or JSON format
- Import tasks from CSV or JSON format
- User authentication and authorization
- Task history and versioning
- Notifications for task updates and deadlines
- Mobile-friendly interface
- Dark mode support
- Multi-language support
- Accessibility features
- Integration with third-party services (e.g., Google Calendar, Trello, etc.)
- Customizable themes and layouts
- Analytics and reporting
- Collaboration features (e.g., comments, attachments, etc.)

## Installation
-----
To update the gRPC Python files, you need to have the `grpcio-tools` package installed. You can then run the following command in the terminal:
```bash
python -m grpc_tools.protoc -I .\toDoList\protos --python_out=.\toDoList\pygrpc --pyi_out=.\toDoList\pygrpc --grpc_python_out=.\toDoList\pygrpc .\toDoList\protos\*
```