from pytube import YouTube

# Function to download YouTube video
def download_video(url, save_path=''):
    try:
        # Create YouTube object
        yt = YouTube(url)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Download the video
        print(f"Downloading: {yt.title}")
        stream.download(output_path=save_path)
        
        print(f"Download completed! Video saved to {save_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
video_url = 'https://www.youtube.com/watch?v=RaG6GgcDt54'  # Replace with your YouTube video URL
download_video(video_url)
