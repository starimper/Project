
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Task } from '../../models/task.model';
import { TaskService } from '../../services/task.service';

@Component({
  selector: 'app-task-edit',
  template: `
    <h2>Edit Task</h2>
    <form *ngIf="task" (ngSubmit)="updateTask()">
      <input [(ngModel)]="task.title" name="title">
      <input [(ngModel)]="task.description" name="description">
      <input [(ngModel)]="task.due_date" name="due_date" type="date">
      <input [(ngModel)]="task.status" name="status" type="number">
      <input [(ngModel)]="task.category" name="category" type="number">
      <button type="submit">Save</button>
    </form>
  `
})
export class TaskEditComponent implements OnInit {
  task!: Task;
  id!: number;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private taskService: TaskService
  ) {}

  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    this.taskService.getTaskById(this.id).subscribe(task => this.task = task);
  }

  updateTask(): void {
    this.taskService.updateTask(this.id, this.task).subscribe(() => {
      this.router.navigate(['/tasks']);
    });
  }
}
