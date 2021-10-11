def write_line_by_line(input_path, output_path, parse):
  input_file = open(input_path, mode="rb")
  output_file = open(output_path, mode="w", encoding="utf-8")
  
  for input_line in input_file:
    output_line = parse(input_line)
    output_file.write(output_line.hex())
  
  input_file.close()
  output_file.close()