
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { TaskListComponent } from './components/task-list/task-list.component';
import { TaskFormComponent } from './components/task-form/task-form.component';
import { TaskEditComponent } from './components/task-edit/task-edit.component';
import { LoginComponent } from './components/login/login.component';

const routes: Routes = [
  { path: 'tasks', component: TaskListComponent },
  { path: 'create', component: TaskFormComponent },
  { path: 'edit/:id', component: TaskEditComponent },
  { path: 'login', component: LoginComponent },
  { path: '', redirectTo: 'tasks', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
