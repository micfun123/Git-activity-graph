import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import requests
import io
from datetime import datetime, timedelta
from PIL import Image, ImageDraw

def get_commits(user, source):
    # can be github or gitlab
    if source == 'github':
        url = f'https://api.github.com/users/{user}/events'
        # Make an API call to GitHub
        response = requests.get(url)
        if response.status_code == 200:
            # Get the commit events for the last 30 days
            payload = response.json()
            payload = payload[:30]
            commit_counts = {}

            # Initialize commit_counts with all dates within the range
            today = datetime.now().date()
            date_range = [today - timedelta(days=i) for i in range(30)]
            for date in date_range:
                commit_counts[date.strftime('%Y-%m-%d')] = 0

            # Process commit events and increment counts
            for obj in payload:
                if obj['type'] == 'PushEvent' and 'commits' in obj['payload']:
                    date = obj['created_at'][:10]
                    if date in commit_counts:
                        commit_counts[date] += len(obj['payload']['commits'])

            return commit_counts

def generate_activity_graph(user,source):
    # Get the date range for the commit counts
    commit_counts = get_commits(user,source)
    start_date = min(commit_counts.keys())
    end_date = max(commit_counts.keys())
    date_range = [datetime.strptime(start_date, '%Y-%m-%d') + timedelta(days=i) for i in range((datetime.strptime(end_date, '%Y-%m-%d') - datetime.strptime(start_date, '%Y-%m-%d')).days + 1)]

    # Create a list of commit counts, including zeros for missing dates
    counts = [commit_counts.get(date.strftime('%Y-%m-%d'), 0) for date in date_range]

    # Set up the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the data
    ax.plot(date_range, counts, color='green')

    # Customize the plot
    ax.set(xlabel='Date', ylabel='Commit Count', title=f'{source} Activity for {user}')
    ax.grid(True)

    # Format the x-axis tick labels
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format the tick labels as dates
    plt.xticks(rotation=45)  # Rotate x-axis tick labels for better readability

    # Save the plot as an image file using Pillow
    image_file = 'activity_graph.png'
    plt.tight_layout()
    plt.savefig(image_file)
    plt.close()

    # Open the image file and display it
    img = Image.open(image_file)
    img.show()
    img.save('activity_graph.png')

# Example usage
print(get_commits('micfun123', 'github'))
generate_activity_graph('micfun123',source='github')

