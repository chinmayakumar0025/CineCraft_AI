import asyncio
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List


class UserTier(Enum):
    FREE = "FREE"
    PREMIUM = "PREMIUM"


@dataclass
class CameraShot:
    shot_type: str = "medium"
    angle: str = "eye-level"
    duration: float = 5.0


@dataclass
class SceneScript:
    raw_prompt: str
    characters: List[str] = field(default_factory=list)
    actions: List[str] = field(default_factory=list)
    environment: str = "default scene"
    camera: CameraShot = field(default_factory=CameraShot)


class NLPSceneParser:

    async def parse_prompt(self, prompt: str) -> SceneScript:
        print(f"\n[NLP Module] Analyzing prompt: '{prompt}'...")
        await asyncio.sleep(0.5)
        script = SceneScript(
            raw_prompt=prompt,
            characters=["Cyber Samurai"],
            actions=["Drawing sword"],
            environment="Futuristic Neon City",
            camera=CameraShot(shot_type="dolly_zoom", duration=4.0),
        )
        return script


class Scene3DGenerator:

    async def build_scene(self, script: SceneScript) -> Dict[str, str]:
        print("\n[3D Engine] Instantiating assets...")
        await asyncio.sleep(0.8)
        return {"env": script.environment}

    async def setup_camera(self, camera_spec: CameraShot) -> str:
        return "camera_rig"


class RenderPipeline:

    async def render_animation(
        self, assets: Dict[str, str], camera: str, tier: UserTier
    ) -> str:
        print("\n[Render Engine] Rendering frames...")
        await asyncio.sleep(1.2)
        if tier == UserTier.FREE:
            print("[Watermark] Applied 'CineCraft AI' watermark.")
            return "output_watermarked.mp4"
        print("[Watermark] Clean output generated.")
        return "output_clean.mp4"


class CineCraftEngine:

    def __init__(self):
        self.nlp = NLPSceneParser()
        self.generator_3d = Scene3DGenerator()
        self.renderer = RenderPipeline()

    async def generate_animation(
        self, prompt: str, tier: UserTier = UserTier.FREE
    ) -> str:
        script = await self.nlp.parse_prompt(prompt)
        assets = await self.generator_3d.build_scene(script)
        camera = await self.generator_3d.setup_camera(script.camera)
        final_file = await self.renderer.render_animation(assets, camera, tier)
        return final_file


if __name__ == "__main__":
    engine = CineCraftEngine()
    prompt = "A samurai drawing his glowing sword."
    asyncio.run(engine.generate_animation(prompt, UserTier.FREE))
    asyncio.run(engine.generate_animation(prompt, UserTier.PREMIUM))

