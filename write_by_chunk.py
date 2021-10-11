def write_by_chunk(input_path, output_path, parse, chunk_size=256):
  output_file = open(output_path, mode="wb")
  
  with open(input_path, "rb") as input_file:
    while (input_line := input_file.read(chunk_size)):
      output_line = parse(input_line)
      output_file.write(output_line)
  
  
  output_file.close()