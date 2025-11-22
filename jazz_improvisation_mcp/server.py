"""
Jazz Improvisation Structure MCP Server
Temporal revelation through established grammar - Monk-centered framework

This server provides tools for enhancing image prompts with jazz improvisation
aesthetic, using categorical structure and intentionality reasoning ologs.
"""

import json
import sys
from pathlib import Path

# Add parent directory to path so imports work
sys.path.insert(0, str(Path(__file__).parent.parent))

from mcp.server import Server
from mcp.types import Tool, TextContent
from typing import Optional

from jazz_improvisation_mcp.olog_loader import JazzImprovisationOlog
from jazz_improvisation_mcp.enhancer import JazzImprovisationEnhancer


# Initialize server and tools
server = Server("jazz-improvisation-mcp")
enhancer = JazzImprovisationEnhancer()


# Tool implementations (separate from decorators for testability)

def impl_enhance_prompt_with_jazz(
    base_prompt: str,
    harmonic_foundation: str = "Round Midnight",
    solo_phase: str = "development",
    intensity_level: int = 5,
    monk_emphasis: bool = True,
) -> dict:
    """Implementation of prompt enhancement"""
    return enhancer.enhance_prompt_with_jazz_structure(
        base_prompt=base_prompt,
        harmonic_foundation=harmonic_foundation,
        solo_phase=solo_phase,
        intensity_level=intensity_level,
        monk_emphasis=monk_emphasis,
    )


def impl_list_harmonic_foundations() -> dict:
    """Implementation of list harmonic foundations"""
    foundations = enhancer.get_all_harmonic_foundations()
    return {
        "foundations": [
            {
                "name": f["name"],
                "complexity": f["complexity"],
                "key_center": f["key_center"],
                "characteristic": f["characteristic"],
                "monk_essence": f.get("monk_essence", False),
            }
            for f in foundations
        ]
    }


def impl_get_harmonic_foundation_details(foundation_name: str) -> dict:
    """Implementation of get harmonic foundation details"""
    olog = JazzImprovisationOlog()
    foundation = olog.get_harmonic_foundation(foundation_name)
    if not foundation:
        return {"error": f"Foundation '{foundation_name}' not found"}
    
    return {
        "name": foundation["name"],
        "complexity": foundation["complexity"],
        "key_center": foundation["key_center"],
        "characteristic": foundation["characteristic"],
        "monk_essence": foundation.get("monk_essence", False),
    }


def impl_get_phase_specification(phase_name: str) -> dict:
    """Implementation of get phase specification"""
    olog = JazzImprovisationOlog()
    phase_spec = olog.get_phase_specification(phase_name)
    if not phase_spec:
        return {"error": f"Phase '{phase_name}' not found. Valid phases: statement, development, resolution"}
    
    return {
        "phase": phase_name,
        "narrative_role": phase_spec.get("narrative_role"),
        "sensory_intention": phase_spec.get("sensory_intention"),
        "what_happens_musically": phase_spec.get("what_happens_musically"),
    }


def impl_compare_phases_intensity(harmonic_foundation: str = "Round Midnight") -> dict:
    """Implementation of compare phases intensity"""
    profiles = enhancer.compare_phases_intensity(harmonic_foundation)
    
    return {
        "harmonic_foundation": harmonic_foundation,
        "phase_comparison": {
            phase: {
                "note_density": profile.get("note_density"),
                "rhythmic_subdivision": profile.get("rhythmic_subdivision"),
                "harmonic_complexity": profile.get("harmonic_complexity"),
                "melodic_singularity": profile.get("melodic_singularity"),
                "rest_space": profile.get("rest_space"),
            }
            for phase, profile in profiles.items()
        }
    }


def impl_get_monk_principles() -> dict:
    """Implementation of get Monk principles"""
    olog = JazzImprovisationOlog()
    principles = olog.get_monk_principles()
    
    return {
        "principles": {
            name: {
                "statement": principle.get("statement"),
                "manifests_as": principle.get("manifests_as"),
            }
            for name, principle in principles.items()
        }
    }


# MCP Tool definitions

@server.list_tools()
async def list_tools() -> list[Tool]:
    """List all available jazz improvisation tools"""
    return [
        Tool(
            name="enhance_prompt_with_jazz",
            description="Enhance an image generation prompt with jazz improvisation aesthetic. Encodes temporal revelation through established harmonic grammar (Monk-centered).",
            inputSchema={
                "type": "object",
                "properties": {
                    "base_prompt": {
                        "type": "string",
                        "description": "The original image description to enhance"
                    },
                    "harmonic_foundation": {
                        "type": "string",
                        "enum": ["Round Midnight", "Evidence", "Epistrophy", "Ask Me Now"],
                        "description": "Which Monk composition to anchor the aesthetic (determines harmonic complexity, characteristic feel)"
                    },
                    "solo_phase": {
                        "type": "string",
                        "enum": ["statement", "development", "resolution"],
                        "description": "Which phase of the solo structure: statement (clarity establishing), development (complexity exploring), resolution (mastery integrating)"
                    },
                    "intensity_level": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 10,
                        "description": "Intensity scale 1-10. Higher = more note density, complexity, dissonance exploration"
                    },
                    "monk_emphasis": {
                        "type": "boolean",
                        "description": "Emphasize Monk-specific principles: dissonance as truth, silence as structure, behind-the-beat mastery"
                    }
                },
                "required": ["base_prompt"]
            }
        ),
        Tool(
            name="list_harmonic_foundations",
            description="List all available harmonic foundations (Monk compositions). Each has specific harmonic complexity and characteristic feel.",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="get_harmonic_foundation_details",
            description="Get detailed information about a specific harmonic foundation including complexity, key center, and characteristic approach.",
            inputSchema={
                "type": "object",
                "properties": {
                    "foundation_name": {
                        "type": "string",
                        "description": "Name of the harmonic foundation (e.g., 'Round Midnight', 'Evidence')"
                    }
                },
                "required": ["foundation_name"]
            }
        ),
        Tool(
            name="get_phase_specification",
            description="Get detailed specification for a solo phase including epistemic role, what happens musically, and why it works.",
            inputSchema={
                "type": "object",
                "properties": {
                    "phase_name": {
                        "type": "string",
                        "enum": ["statement", "development", "resolution"],
                        "description": "Which solo phase to get specification for"
                    }
                },
                "required": ["phase_name"]
            }
        ),
        Tool(
            name="compare_phases_intensity",
            description="Compare intensity profiles (note density, harmonic complexity, etc.) across all three solo phases for a given harmonic foundation.",
            inputSchema={
                "type": "object",
                "properties": {
                    "harmonic_foundation": {
                        "type": "string",
                        "enum": ["Round Midnight", "Evidence", "Epistrophy", "Ask Me Now"],
                        "description": "Which harmonic foundation to use for comparison"
                    }
                }
            }
        ),
        Tool(
            name="get_monk_principles",
            description="Get Monk-specific anchor principles: constraint as liberation, silence as structure, rhythmic displacement, dissonance as truth.",
            inputSchema={"type": "object", "properties": {}}
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Execute a tool and return results"""
    
    if name == "enhance_prompt_with_jazz":
        result = impl_enhance_prompt_with_jazz(**arguments)
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    elif name == "list_harmonic_foundations":
        result = impl_list_harmonic_foundations()
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    elif name == "get_harmonic_foundation_details":
        result = impl_get_harmonic_foundation_details(arguments["foundation_name"])
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    elif name == "get_phase_specification":
        result = impl_get_phase_specification(arguments["phase_name"])
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    elif name == "compare_phases_intensity":
        foundation = arguments.get("harmonic_foundation", "Round Midnight")
        result = impl_compare_phases_intensity(foundation)
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    elif name == "get_monk_principles":
        result = impl_get_monk_principles()
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    else:
        return [TextContent(type="text", text=json.dumps({"error": f"Unknown tool: {name}"}))]

def run_server():
    """Entry point for console script"""
    import asyncio
    asyncio.run(server.run())

    
def main():
    """Run the MCP server"""
    import asyncio
    asyncio.run(server.run())


if __name__ == "__main__":
    main()
