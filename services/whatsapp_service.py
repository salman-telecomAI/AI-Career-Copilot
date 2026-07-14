import pywhatkit


def send_whatsapp_notification(job):
    """
    Sends a WhatsApp message using WhatsApp Web.
    """

    message = f"""
🤖 AI Career Copilot

New Job Found

Company: {job.company}
Role: {job.title}
Location: {job.location}
Salary: {job.salary}
Match Score: {job.match_score}%

Reply:
APPROVE
or
REJECT
"""

    phone_number = "+923335289080"  # Replace with your own number

    pywhatkit.sendwhatmsg_instantly(
        phone_number,
        message,
        wait_time=15,
        tab_close=True,
        close_time=5,
    )
