import sys 
import service

def main():
    list = sys.argv
    input_file_path = list[1]
    output_file_path = list[2]
    output_html = service.convert_to_html(input_file_path)
    service.create_html_file(output_html, output_file_path)
    
if __name__ == "__main__":
    main()