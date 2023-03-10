from django.urls import path
from leave_tracker.views import (
    EmployeeCreateView,
    EmployeeListView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    LeaveApplyView,
)

urlpatterns = [
    path('leave_tracker/create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('leave_tracker/list/', EmployeeListView.as_view(), name='employee-list'),
    path('leave_tracker/update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('leave_tracker/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('leave_tracker/apply/', LeaveApplyView.as_view(), name='leave-apply'),
]
