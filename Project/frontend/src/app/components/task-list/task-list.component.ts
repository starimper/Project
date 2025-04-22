
import { Component, OnInit } from '@angular/core';
import { TaskService } from '../../services/task.service';
import { Task } from '../../models/task.model';
import { Router } from '@angular/router';

@Component({
  selector: 'app-task-list',
  template: \`
    <h2>Task List</h2>
    <div *ngFor="let task of tasks">
      <strong>{{ task.title }}</strong> — {{ task.description }}
      <button (click)="editTask(task.id)">Edit</button>
      <button (click)="deleteTask(task.id)">Delete</button>
    </div>
  \`
})
export class TaskListComponent implements OnInit {
  tasks: Task[] = [];

  constructor(private taskService: TaskService, private router: Router) {}

  ngOnInit(): void {
    this.taskService.getTasks().subscribe(data => this.tasks = data);
  }

  deleteTask(id: number): void {
    this.taskService.deleteTask(id).subscribe(() => {
      this.tasks = this.tasks.filter(t => t.id !== id);
    });
  }

  editTask(id: number): void {
    this.router.navigate(['/edit', id]);
  }
}
