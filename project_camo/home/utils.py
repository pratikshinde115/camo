from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_thank_you_email(email, name):
    context = {
        'customer_name': name,
    }

    # Render the HTML template with context data
    html_content = render_to_string('email_connecting.html', context)

    # Send email
    send_mail(
        'Subject of the Email',
        '',  # Empty body as we are using html_content
        'pratik.shinde@buypolicynow.com',  # From email
        [email],  # List of recipients
        html_message=html_content,  # Attach HTML content
        fail_silently=False,
    )

# Example usage
