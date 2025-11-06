def update_server_config(file_path, key, new_value):
   
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file: 
         for line in lines:
                if key in line:
                     line = file.write(key + "=" + new_value + "\n")
                else:
                    file.write(line)

    print("Configuration updated successfully.")


update_server_config("server.conf","MAX_CONNECTIONS","850")