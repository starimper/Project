
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Task } from '../../models/task.model';
import { TaskService } from '../../services/task.service';

@Component({
  selector: 'app-task-form',
  template: `
    <h2>Create Task</h2>
    <form (ngSubmit)="onSubmit()">
      <input [(ngModel)]="task.title" name="title" placeholder="Title">
      <input [(ngModel)]="task.description" name="description" placeholder="Description">
      <input [(ngModel)]="task.due_date" name="due_date" type="date">
      <select [(ngModel)]="task.importance" name="importance">
        <option [value]="1">Low</option>
        <option [value]="2">Medium</option>
        <option [value]="3">High</option>
      </select>
      <input [(ngModel)]="task.status" name="status" type="number" placeholder="Status ID">
      <input [(ngModel)]="task.category" name="category" type="number" placeholder="Category ID">
      <button type="submit">Create</button>
    </form>
  `
})
export class TaskFormComponent {
  task: Task = {
    title: '',
    description: '',
    due_date: '',
    importance: 1,
    status: 1,
    category: 1
  };

  constructor(private taskService: TaskService, private router: Router) {}

  onSubmit(): void {
    this.taskService.createTask(this.task).subscribe(() => {
      this.router.navigate(['/tasks']);
    });
  }
}
