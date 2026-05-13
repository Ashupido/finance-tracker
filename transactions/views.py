from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
import datetime
import csv
from .models import Transaction, Budget
from .forms import TransactionForm, BudgetForm

@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transactions/list.html', {'transactions': transactions})

@login_required
def transaction_add(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transactions/form.html', {'form': form, 'title': 'Add Transaction'})

@login_required
def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transactions/form.html', {'form': form, 'title': 'Edit Transaction'})

@login_required
def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'transactions/confirm_delete.html', {'transaction': transaction})

@login_required
def budget_list(request):
    today = datetime.date.today()
    first_of_month = today.replace(day=1)

    budgets = Budget.objects.filter(user=request.user, month=first_of_month)

    budget_data = []
    for budget in budgets:
        spent = Transaction.objects.filter(
            user=request.user,
            category=budget.category,
            type='expense',
            date__year=today.year,
            date__month=today.month,
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        percentage = 0
        if budget.limit and float(budget.limit) != 0:
            percentage = min(int((float(spent) / float(budget.limit)) * 100), 100)
        budget_data.append({
            'budget': budget,
            'spent': spent,
            'percentage': percentage,
            'over': spent > budget.limit,
        })

    return render(request, 'transactions/budget_list.html', {'budget_data': budget_data})

@login_required
def budget_add(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.month = budget.month.replace(day=1)
            budget.save()
            return redirect('budget_list')
    else:
        form = BudgetForm()
    return render(request, 'transactions/budget_form.html', {'form': form})

@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Title', 'Category', 'Type', 'Amount', 'Description'])

    transactions = Transaction.objects.filter(user=request.user)
    for t in transactions:
        writer.writerow([t.date, t.title, t.category, t.type, t.amount, t.description])

    return response
