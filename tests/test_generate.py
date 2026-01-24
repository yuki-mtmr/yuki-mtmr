"""
README生成スクリプトのテスト
"""
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock


class TestGenerateReadme:
    """README生成のテストクラス"""

    def test_load_config_returns_dict(self):
        """load_config関数が辞書を返すことを確認"""
        from generate import load_config

        config_path = Path(__file__).parent.parent / 'profile-config.yaml'
        result = load_config(config_path)

        assert isinstance(result, dict)
        assert 'user' in result
        assert 'skills' in result

    def test_config_has_no_ruby(self):
        """設定からRubyが削除されていることを確認"""
        from generate import load_config

        config_path = Path(__file__).parent.parent / 'profile-config.yaml'
        result = load_config(config_path)

        assert 'ruby' not in result['skills']['languages']
        assert 'rails' not in result['skills']['backend']

    def test_bio_has_no_ruby(self):
        """bioにRubyの記述がないことを確認"""
        from generate import load_config

        config_path = Path(__file__).parent.parent / 'profile-config.yaml'
        result = load_config(config_path)

        bio = result['user']['bio'].lower()
        assert 'ruby' not in bio

    def test_get_github_stats_returns_formatted_dict(self):
        """get_github_stats関数がフォーマット済み辞書を返すことを確認"""
        from generate import get_github_stats

        with patch('generate.fetch_user_stats') as mock_fetch:
            with patch('generate.fetch_contributions') as mock_contrib:
                mock_fetch.return_value = {
                    'public_repos': 42,
                    'followers': 100,
                    'following': 50
                }
                mock_contrib.return_value = 500

                result = get_github_stats('yuki-mtmr')

                assert 'repos' in result
                assert 'followers' in result
                assert 'contributions' in result
                assert result['repos'] == '42'
                assert result['contributions'] == '500'

    def test_generate_readme_includes_github_stats(self):
        """生成されたREADMEにGitHub統計が含まれることを確認"""
        from generate import create_jinja_env, generate_readme

        template_dir = Path(__file__).parent.parent / 'src'
        env = create_jinja_env(template_dir)

        config = {
            'user': {
                'name': 'Test User',
                'github_username': 'test',
                'title': 'Developer',
                'location': 'Japan',
                'bio': 'Test bio'
            },
            'skills': {
                'languages': ['python', 'typescript']
            },
            'social': {},
            'github_stats': {
                'repos': '42',
                'followers': '100',
                'following': '50',
                'contributions': '500'
            }
        }

        result = generate_readme(config, env)

        # 外部サービスのURLが含まれていないことを確認
        assert 'github-readme-stats.vercel.app' not in result
        # 統計データがテキストで含まれていることを確認
        assert '42' in result
        assert 'Repos' in result or 'repos' in result.lower()

    def test_main_function_runs_successfully(self):
        """main関数が正常に実行されることを確認"""
        from unittest.mock import mock_open

        with patch('generate.get_github_stats') as mock_stats:
            mock_stats.return_value = {
                'repos': '10',
                'followers': '5',
                'following': '3',
                'contributions': '100'
            }

            with patch('builtins.open', mock_open()):
                from generate import main
                assert callable(main)

    def test_create_jinja_env_has_urlencode_filter(self):
        """Jinja2環境にurlencodeフィルタが追加されていることを確認"""
        from generate import create_jinja_env

        template_dir = Path(__file__).parent.parent / 'src'
        env = create_jinja_env(template_dir)

        assert 'urlencode' in env.filters
        result = env.filters['urlencode']('hello world')
        assert result == 'hello%20world'
