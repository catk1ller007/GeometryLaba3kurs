def writeFile_time(file_path1, arrpoints, timik):
    with open(file_path1, 'w') as file:
        file.write(f"{arrpoints} {timik}")