import tempfile
from unittest import TestCase
import os
from pathlib import Path
from capanno_utils import repo_config
from capanno_utils.content_maps import make_tools_map, make_workflow_maps, make_script_maps
from capanno_utils.helpers.file_management import dump_dict_to_yaml_output

test_constants = {'script_group1': 'ENCODE-DCC', 'script_version1': '1.1.x', 'script_project1': 'atac-seq-pipeline',
                  'test_software_version': {'versionName': 'test_version'}}


class TestBase(TestCase):
    projects_path = Path(__file__).parents[2]
    src_content_dir = projects_path / repo_config.content_repo_name
    test_files_dir = Path(__file__).parent / 'test_files'
    test_content_dir = Path(__file__).parent / 'test_files' / repo_config.content_repo_name
    invalid_content_dir = Path(__file__).parent / 'test_files' / 'invalid_content'  # Will copy data here, then modify to make invalid.

    def get_content_map_paths(self):
        return {'tool_maps': repo_config.config[os.environ.get('CONFIG_KEY')]['content_maps_dir'] / repo_config.tools_map_name,
                'script_maps': repo_config.config[os.environ.get('CONFIG_KEY')]['content_maps_dir'] / 'script-maps.yaml',
                'workflow_maps': repo_config.config[os.environ.get('CONFIG_KEY')]['content_maps_dir'] / 'workflow-maps.yaml'}


    def update_tool_maps(self):
        outfile_path = self.get_content_map_paths()['tool_maps']
        make_tools_map(outfile_path)

    def update_script_maps(self):
        outfile_path = self.get_content_map_paths()['script_maps']
        make_script_maps(outfile_path)

    def update_workflow_maps(self):
        outfile_path = self.get_content_map_paths()['workflow_maps']
        make_workflow_maps(outfile_path)

    def make_empty_tools_index(self, output_dir):
        output_dir = Path(output_dir)
        tools_index_dir = output_dir / repo_config.identifier_index_dir
        tools_index_dir.mkdir()
        tool_index_path = output_dir / repo_config.tool_index_path
        tool_index_path.touch()
        return

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()

    def tearDown(self) -> None:
        pass
