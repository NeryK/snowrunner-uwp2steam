"""Automate Snowrunner save file renaming described in https://blog.s505.su/2021/08/how-to-transfer-snowrunner-game-saves.html"""
import argparse
import struct
import os
import shutil
from sr_u2s import container


def copy_file(input_dir, input_name, output_dir, output_name, dry_run):
    input = os.path.join(input_dir, input_name)
    output = os.path.join(output_dir, f"{output_name}.cfg")
    print(f"Copy {input} to {output}")
    if not dry_run:
        shutil.copy2(input, output)

def copy_rename_save(save_list, input_dir, output_dir, dry_run):
    for decoded_filename, hashed_filename in save_list:
        copy_file(input_dir, hashed_filename, output_dir, decoded_filename, dry_run)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename Snowrunner save files from Windows Store to Steam convention")
    parser.add_argument("--input-container", help="UWP container.xyz file", required=True)
    parser.add_argument("--input-save-directory", help="Snowrunner Windows Store savegame directory", required=True)
    parser.add_argument("--output-save-directory", help="Snowrunner Steam savegame directory", required=True)
    parser.add_argument("--dry-run", action="store_true", default=False, help="Enable dry run, do not copy files")
    args = parser.parse_args()

    save_list = container.load_container(args.input_container)
    #print(save_list)
    if not os.path.exists(args.input_save_directory) or not os.path.isdir(args.input_save_directory):
        parser.error(f"Error accessing {args.input_save_directory}")
    if not args.dry_run:
        os.makedirs(args.output_save_directory, exist_ok=True)
    copy_rename_save(save_list, args.input_save_directory, args.output_save_directory, args.dry_run)
