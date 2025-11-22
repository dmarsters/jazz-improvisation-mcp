"""
Jazz Improvisation Structure MCP Server
Temporal revelation through established grammar - Monk-centered framework
"""

import json
import sys
import yaml
from pathlib import Path
from mcp.server import Server
from mcp.types import Tool, TextContent
from typing import Optional

# Get the directory where this file is located
CURRENT_DIR = Path(__file__).parent

# Import from local modules directly
sys.path.insert(0, str(CURRENT_DIR))

try:
    from olog_loader import JazzImprovisationOlog
    from enhancer import JazzImprovisationEnhancer
except ImportError as e:
    print(f"Import error: {e}")
    raise

# Initialize
app = Server("jazz-improvisation-mcp")
enhancer = JazzImprovisationEnhancer()

# Tool implementations
def impl_enhance_prompt_with_jazz(base_prompt: str, harmonic_foundation: str = "Round Midnight", 
                                   solo_phase: str = "development", intensity_level: int = 5, 
                                   monk_emphasis: bool = True) -> dict:
    return enhancer.enhance_prompt_with_jazz_structure(
        base_prompt=base_prompt,
        harmonic_foundation=harmonic_foundation,
        solo_phase=solo_phase,
        intensity_level=intensity_level,
        monk_emphasis=monk_emphasis,
    )

def impl_list_harmonic_foundations() -> dict:
    foundations = enhancer.get_all_harmonic_foundations()
    return {"foundations": [{"name": f["name"], "complexity": f["complexity"], "key_center": f["key_center"], 
                             "characteristic": f["characteristic"], "monk_essence": f.get("monk_essence", False)} for f in foundations]}

def impl_get_harmonic_foundation_details(foundation_name: str) -> dict:
    olog = JazzImprovisationOlog()
    foundation = olog.get_harmonic_foundation(foundation_name)
    if not foundation:
        return {"error": f"Foundation '{foundation_name}' not found"}
    return {"name": foundation["name"], "complexity": foundation["complexity"], "key_center": foundation["key_center"], 
            "characteristic": foundation["characteristic"], "monk_essence": foundation.get("monk_essence", False)}

def impl_get_phase_specification(phase_name: str) -> dict:
    olog = JazzImprovisationOlog()
    phase_spec = olog.get_phase_specification(phase_name)
    if not phase_spec:
        return {"error": f"Phase '{phase_name}' not found"}
    return {"phase": phase_name, "narrative_role": phase_spec.get("narrative_role"), 
            "sensory_intention": phase_spec.get("sensory_intention"), 
            "what_happens_musically": phase_spec.get("what_happens_musically")}

def impl_compare_phases_intensity(harmonic_foundation: str = "Round Midnight") -> dict:
    profiles = enhancer.compare_phases_intensity(harmonic_foundation)
    return {"harmonic_foundation": harmonic_foundation, 
            "phase_comparison": {phase: {k: v for k, v in profile.items() if k in ["note_density", "rhythmic_subdivision", "harmonic_complexity", "melodic_singularity", "rest_space"]} 
                                for phase, profile in profiles.items()}}

def impl_get_monk_principles() -> dict:
    olog = JazzImprovisationOlog()
    principles = olog.get_monk_principles()
    return {"principles": {name: {"statement": principle.get("statement"), "manifests_as": principle.get("manifests_as")} 
                          for name, principle in principles.items()}}

# Tool definitions
@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(name="enhance_prompt_with_jazz", description="Enhance an image generation prompt with jazz improvisation aesthetic.",
             inputSchema={"type": "object", "properties": {"base_prompt": {"type": "string", "description": "The original image description to enhance"},
                                                            "harmonic_foundation": {"type": "string", "enum": ["Round Midnight", "Evidence", "Epistrophy", "Ask Me Now"],
                                                                                   "description": "Which Monk composition to anchor"},
                                                            "solo_phase": {"type": "string", "enum": ["statement", "development", "resolution"],
                                                                         "description": "Which phase of solo structure"},
                                                            "intensity_level": {"type": "integer", "minimum": 1, "maximum": 10,
                                                                              "description": "Intensity scale 1-10"},
                                                            "monk_emphasis": {"type": "boolean", "description": "Emphasize Monk-specific principles"}},
                         "required": ["base_prompt"]}),
        Tool(name="list_harmonic_foundations", description="List all available harmonic foundations (Monk compositions).",
             inputSchema={"type": "object", "properties": {}}),
        Tool(name="get_harmonic_foundation_details", description="Get detailed information about a specific harmonic foundation.",
             inputSchema={"type": "object", "properties": {"foundation_name": {"type": "string", "description": "Name of the harmonic foundation"}},
                         "required": ["foundation_name"]}),
        Tool(name="get_phase_specification", description="Get detailed specification for a solo phase.",
             inputSchema={"type": "object", "properties": {"phase_name": {"type": "string", "enum": ["statement", "development", "resolution"],
                                                                         "description": "Which solo phase to get specification for"}},
                         "required": ["phase_name"]}),
        Tool(name="compare_phases_intensity", description="Compare intensity profiles across all three solo phases.",
             inputSchema={"type": "object", "properties": {"harmonic_foundation": {"type": "string", "enum": ["Round Midnight", "Evidence", "Epistrophy", "Ask Me Now"],
                                                                                   "description": "Which harmonic foundation to use for comparison"}}}),
        Tool(name="get_monk_principles", description="Get Monk-specific anchor principles.",
             inputSchema={"type": "object", "properties": {}}),
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "enhance_prompt_with_jazz":
        result = impl_enhance_prompt_with_jazz(**arguments)
    elif name == "list_harmonic_foundations":
        result = impl_list_harmonic_foundations()
    elif name == "get_harmonic_foundation_details":
        result = impl_get_harmonic_foundation_details(arguments["foundation_name"])
    elif name == "get_phase_specification":
        result = impl_get_phase_specification(arguments["phase_name"])
    elif name == "compare_phases_intensity":
        result = impl_compare_phases_intensity(arguments.get("harmonic_foundation", "Round Midnight"))
    elif name == "get_monk_principles":
        result = impl_get_monk_principles()
    else:
        result = {"error": f"Unknown tool: {name}"}
    
    return [TextContent(type="text", text=json.dumps(result, indent=2))]


