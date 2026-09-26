import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs =os.path.abspath(working_directory)

        target_directory = os.path.normpath(os.path.join(working_dir_abs, directory))

        valid_target_dir = os.path.commonpath(
            [working_dir_abs, target_directory]
        ) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'

        items = os.listdir(target_directory)
        results = []

        for item in items:
            item_path = os.path.join(target_directory, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            line = f"- {item}: file_size={file_size} bytes, is_dir={is_dir}"
            results.append(line)
        return "\n".join(results)

    except Exception as e:
        return f'Error: {e}'
