from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transactions.models import Transaction
from django.db.models import Sum
import json

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)

    # Total income and expense
    total_income = transactions.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = transactions.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense

    # Spending by category (for pie chart)
    expense_by_category = (
        transactions.filter(type='expense')
        .values('category__name')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )
    pie_labels = [item['category__name'] for item in expense_by_category]
    pie_data = [float(item['total']) for item in expense_by_category]

    # Last 5 transactions
    recent_transactions = transactions[:5]

    context = {
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'pie_labels': json.dumps(pie_labels),
        'pie_data': json.dumps(pie_data),
        'recent_transactions': recent_transactions,
    }
    return render(request, 'dashboard/dashboard.html', context)