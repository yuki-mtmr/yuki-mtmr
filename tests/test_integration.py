"""
統合テスト: main関数の実行テスト
"""
import pytest
from pathlib import Path
from unittest.mock import patch


class TestIntegration:
    """統合テストクラス"""

    def test_main_generates_readme_without_ruby(self):
        """main関数がRuby/Railsなしで生成することを確認"""
        with patch('generate.fetch_user_stats') as mock_stats:
            with patch('generate.fetch_contributions') as mock_contrib:
                mock_stats.return_value = {
                    'public_repos': 10,
                    'followers': 5,
                    'following': 3,
                    'public_gists': 0
                }
                mock_contrib.return_value = 100

                from generate import main
                main()

                readme_path = Path(__file__).parent.parent / 'README.md'
                with open(readme_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                assert 'Ruby' not in content
                assert 'Rails' not in content
                assert 'github-readme-stats.vercel.app' not in content
                assert '10' in content
                assert 'Repos' in content

    def test_generated_readme_has_valid_structure(self):
        """生成されたREADMEが正しい構造を持つことを確認"""
        with patch('generate.fetch_user_stats') as mock_stats:
            with patch('generate.fetch_contributions') as mock_contrib:
                mock_stats.return_value = {
                    'public_repos': 42,
                    'followers': 100,
                    'following': 50,
                    'public_gists': 0
                }
                mock_contrib.return_value = 500

                from generate import main
                main()

                readme_path = Path(__file__).parent.parent / 'README.md'
                with open(readme_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                assert '## Hi there' in content
                assert '### About Me' in content
                assert '### Tech Stack' in content
                assert '### GitHub Stats' in content
                assert '| 📊 Stats | Count |' in content
