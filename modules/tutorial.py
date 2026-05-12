import core

class Tutorial(core.module.Module):
    """Guides you through openlumara if you're new!"""

    async def on_system_prompt(self):
        output = []

        disable_instr = "by typing `/module tutorial`"
        webui_instr = ""
        if "webui" in self.manager.channels:
            webui_host = self.manager.channels["webui"].config.get("host")
            webui_port = self.manager.channels["webui"].config.get("port")

            webui_instr = f"""
Ask the user if they need any help with setting up openlumara. If user says yes, follow these instructions: To set up openlumara, the user needs to open the webui's settings dialog (gear icon at the top of the chat window in the webUI). If the user is not currently in the webUI, tell them to open the webUI at `http://{webui_host}:{webui_port}`. Then inside the settings dialog, the most important thing is that the user can toggle channels and modules, and set up settings to their liking per channel and per module.
            """.strip()
            disable_instr += " or through the WebUI's settings dialog, in the Modules section"

        output.append(f"""
ALWAYS upon the first message of a conversation, tell the user how to use openlumara by referencing the channel instructions within your system prompt. Present the information in a user-friendly, easy to understand way.

Also, tell the user: This tutorial message can be turned off by disabling the tutorial module, which the user can do {disable_instr}. Tell the user modules can insert system prompts like this tutorial, add new commands for the user to use, do things when the user or the AI sends a message, run anything in the background, and other cool stuff. And that a module called `module_maker` is available which can automatically code modules for the user, replacing the `SKILL.md` system used in many other popular AI agents.

{webui_instr}
""")

        return "\n".join(output)
