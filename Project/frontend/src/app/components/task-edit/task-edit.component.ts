
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { TaskService } from '../../services/task.service';
import { Task } from '../../models/task.model';

@Component({
  selector: 'app-task-edit',
  templateUrl: './task-edit.component.html'
})
export class TaskEditComponent implements OnInit {
  task: Task = {
    title: '',
    description: '',
    due_date: '',
    importance: 1,
    status: 1,
    category: 1
  };
  id!: number;

  constructor(
    private taskService: TaskService,
    private route: ActivatedRoute,
    private router: Router
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
