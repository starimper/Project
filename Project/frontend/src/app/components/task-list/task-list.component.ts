
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { TaskService } from '../../services/task.service';
import { Task } from '../../models/task.model';

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})
export class TaskListComponent implements OnInit {
  tasks: Task[] = [];
  filteredTasks: Task[] = [];

  constructor(private taskService: TaskService, private router: Router) {}

  ngOnInit(): void {
    this.taskService.getTasks().subscribe(data => {
      this.tasks = data;
      this.filteredTasks = data;
    });
  }

  onFilterChange(value: string): void {
    const val = parseInt(value);
    this.filteredTasks = val ? this.tasks.filter(task => task.importance === val) : this.tasks;
  }

  deleteTask(id: number): void {
    if (confirm('Are you sure?')) {
      this.taskService.deleteTask(id).subscribe(() => {
        this.filteredTasks = this.filteredTasks.filter(t => t.id !== id);
      });
    }
  }

  editTask(id: number): void {
    this.router.navigate(['/edit', id]);
  }
}
