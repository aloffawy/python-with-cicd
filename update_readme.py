import datetime

def update_readme():
    # Get the current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Update the README file
    with open("README.md", "w") as readme_file:
        readme_file.write(f"# Daily Update\n\nLast updated on {current_time}\n")
    
    print(f"README.md updated at {current_time}")

if __name__ == "__main__":
    update_readme()
