from pathlib import Path
from dataclasses import dataclass

"""
A simple local python package to simplify automated generation of media for docs
"""

@dataclass(frozen=True)
class Env:
    assets_path: Path
    
    @staticmethod
    def Get() -> Env:
        import dotenv
        env_values = dotenv.dotenv_values(dotenv.find_dotenv())
        return Env(assets_path=Path(env_values.get("assets_path", Path("docs/assets")))) # type: ignore

@dataclass(frozen=True)
class Paths:
    assets: Path
    animations: Path
    audio: Path
    images: Path
    src: Path
    thumbnails: Path
    videos: Path
    
    @staticmethod
    def Get() -> Paths:
        env = Env.Get()
        return Paths(
            assets = env.assets_path,
            animations = env.assets_path / 'animations',
            audio = env.assets_path / 'audio',
            images = env.assets_path / 'images',
            src = env.assets_path / 'src',
            thumbnails = env.assets_path / 'thumbnails',
            videos = env.assets_path / 'videos'
        )