from django.db import models

TASK_CHOICES = [
    ('N', 'New'),
    ('I', 'In Progress'),
    ('P', 'Pending'),
    ('B', 'Blocked'),
    ('D', 'Done'),
]


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование задачи', unique=True)
    description = models.TextField(verbose_name="Описание задачи")
    categories = models.ManyToManyField('Category')
    status = models.CharField(max_length=50, choices=TASK_CHOICES, verbose_name="Тип задачи")
    deadline = models.DateField(verbose_name="Срок выполнения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время начала выполнения")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_task'
        ordering = ['-created_at']
        verbose_name = 'Task'


class SubTask(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование подзадачи', unique=True)
    description = models.TextField(verbose_name="Описание подзадачи")
    task = models.ForeignKey('Task', on_delete=models.CASCADE, verbose_name='Основная задача')
    status = models.CharField(max_length=50, choices=TASK_CHOICES, verbose_name="Тип подзадачи")
    deadline = models.DateField(verbose_name="Срок выполнения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время начала выполнения")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ['-created_at']
        verbose_name = 'Subtask'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Наименование категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
