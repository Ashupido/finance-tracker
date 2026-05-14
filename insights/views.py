from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from transactions.models import Transaction
from django.db.models import Sum


@login_required
def chat(request):
    """Chat view for AI insights on user finances."""
    response_text = None
    error_message = None
    
    if request.method == 'POST':
        user_prompt = request.POST.get('prompt', '').strip()
        
        if not user_prompt:
            error_message = "Please enter a question."
        else:
            try:
                # Get user financial summary
                income_total = Transaction.objects.filter(
                    user=request.user, type='income'
                ).aggregate(total=Sum('amount'))['total'] or 0
                
                expense_total = Transaction.objects.filter(
                    user=request.user, type='expense'
                ).aggregate(total=Sum('amount'))['total'] or 0
                
                transaction_count = Transaction.objects.filter(user=request.user).count()
                balance = income_total - expense_total
                
                # Generate simple response
                response_text = f"""📊 Financial Summary & Analysis

Your Question: "{user_prompt}"

💰 Current Status:
• Total Income: ${income_total:,.2f}
• Total Expenses: ${expense_total:,.2f}
• Balance: ${balance:,.2f}
• Total Transactions: {transaction_count}

💡 Insights:
Based on your current financial data:
1. You have {transaction_count} transactions recorded
2. Your current balance is ${balance:,.2f}
3. Your spending-to-income ratio is {(expense_total/income_total*100 if income_total > 0 else 0):.1f}%

📝 Suggestions:
• Review your recent transactions in the Transactions tab
• Check your budget status in the Budgets section
• Use the Export CSV feature to analyze spending patterns
• Track your monthly trends in the Dashboard

💳 To unlock full AI analysis:
Set up billing on your OpenAI account and disable DEMO_MODE in .env"""

            except Exception as e:
                error_message = f"Error: {str(e)}"
    
    return render(request, 'insights/chat.html', {
        'response': response_text,
        'error': error_message,
    })



