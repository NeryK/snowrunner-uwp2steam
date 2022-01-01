"""Module entry point"""
import os
import argparse
import pathlib
from sr_u2s import __doc__, __version__
from sr_u2s import container, remotecache, transfer_save


def locate_container(input_dir):
    save_path = pathlib.Path(input_dir)
    files = [f for f in save_path.glob("container.*") if f.is_file()]
    if len(files) != 1:
        raise FileNotFoundError(f"No single 'container.XYZ' file found in {input_dir}")
    return str(files[0])

def make_remotecache(output_subdir):
    save_path = pathlib.Path(output_subdir)
    remcache_path = pathlib.Path(os.path.join(save_path.parent, "remotecache.vdf"))
    remotecache.write_remcache(remcache_path, save_path)
    return str(remcache_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-i", "--input-uwp-save-directory", help="Snowrunner Windows Store savegame directory", required=True)
    parser.add_argument("-o", "--output-steam-save-directory", help="Snowrunner Steam savegame directory", required=True)
    parser.add_argument("-v", "--version", action="version", version=__version__)
    args = parser.parse_args()

    print("Snowrunner save UWP -> Steam start.")
    input_dir = args.input_uwp_save_directory
    if not os.path.exists(input_dir) or not os.path.isdir(input_dir):
        parser.error(f"Error accessing {input_dir}")
    container_path = locate_container(input_dir)
    save_list = container.load_container(locate_container(input_dir))
    print(f"Container file {container_path} loaded.")
    output_subdir = os.path.join(args.output_steam_save_directory, "1465360", "remote")
    os.makedirs(output_subdir, exist_ok=True)
    transfer_save.copy_rename_save(save_list, input_dir, output_subdir, False)
    print(f"{len(save_list)} files copied.")
    remcache_file = make_remotecache(output_subdir)
    print(f"Steam remote cache generated ({remcache_file}).")
    print("Snowrunner save UWP -> Steam end.")
