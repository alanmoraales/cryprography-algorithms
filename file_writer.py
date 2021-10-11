import time


class FileWriter:
    @staticmethod
    def transform_by_chunk(input_path, output_path, parse, chunk_size=256):
        output_file = open(output_path, mode="wb")

        with open(input_path, "rb") as input_file:
            while input_line := input_file.read(chunk_size):
                output_line = parse(input_line)
                output_file.write(output_line)

        output_file.close()

    @staticmethod
    def with_measure_time(func):
        start_time = time.time()
        response = func()
        end_time = time.time()
        measured_time = end_time - start_time
        return [measured_time, response]

    @staticmethod
    def write_file(file_dir, content):
        file = open(file_dir, "w", encoding="utf-8", newline="")
        file.write(content)
        file.close()

    @staticmethod
    def write_line_by_line(input_path, output_path, parse):
        input_file = open(input_path, mode="rb")
        output_file = open(output_path, mode="w", encoding="utf-8")

        for input_line in input_file:
            output_line = parse(input_line)
            output_file.write(output_line.hex())

        input_file.close()
        output_file.close()
