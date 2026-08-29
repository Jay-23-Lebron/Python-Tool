"""
Basic Python practice demo
Contains string, dictionary, file I/O examples
"""

def string_demo():
    message=" Hello World "
    clean_msg=message.strip()

    replaced_msg=clean_msg.replace("World","Python")
    print(f"After replace |{replaced_msg}|")

    slice_part=clean_msg[0:5]
    print(f"Sliced result |{slice_part}|")

    split_result=clean_msg.split(" ")
    print(f"Split result {split_result}")
   

    upper_msg=message.upper()
    lower_msg=message.lower()

    print(f"Original: {message}")
    print(f"After strip |{clean_msg}|")
    print(f"Upper: {upper_msg}")
    print(f"Lower: {lower_msg}")

    return upper_msg

def dict_demo():
    student={"name":"Tom","age":20,"major":"Computer Science"}
    print(f"Original dict: {student}")

    student_name=student["name"]
    print(f"GEt value by key 'name': {student_name}")

    student["age"]=21
    print(f"Dict after update age: {student}")

    student["grade"]="A"
    print(f"Dict after add new key: {student}")

    print("\nLoop through dictionary items:")
    for key, value in student.items():
        print(f"Key: {key}, Value: {value}")

    del student["grade"]
    print(f"Dict after delete 'grade': {student}")
    return

def file_demo():
        content="Hello file system\nPython dictionary practice done"
        with open("demo_output.txt","w") as f:
            f.write(content)
        print("Finished writing to file")

        with open("demo_output.txt","r") as f:
            read_text=f.read()

        print("\nContent read from file:")
        print(read_text)
        

if __name__ == "__main__":
    string_demo()
    dict_demo()
    file_demo()