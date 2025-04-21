
export interface Task {
  id?: number;
  title: string;
  description: string;
  due_date: string;
  importance: number;
  status: number;
  category: number;
  user?: number;
}
