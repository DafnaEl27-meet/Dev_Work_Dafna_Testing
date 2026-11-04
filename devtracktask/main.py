
import flet as ft
import flet_audio as fta


async def main(page: ft.Page):

    page.bgcolor = "#FFFFFF"

    # Counter
    counter = ft.Text("0", size=60, data=0, color="#000000")

    # End credits
    end_credits_text = ft.Text(
        "END CREDITS\n\nCoding: Dafna \nAudio clips: Gali (my sister) \nScript: Dafna & Gali \nInspired by: Formula 1 \nAll rights reserved to 2026 Tamagochi",
        size=28,
        color="#FFFF00",
        visible=False,
        text_align=ft.TextAlign.CENTER,
    )

    # Oscar Easter egg message
    easter_egg_text = ft.Text(
        "You've reached the land down under. \nWelcome to Oscarland. \ncongrats",
        size=20,
        color="#222222",
        visible=False,
        text_align=ft.TextAlign.CENTER,
    )

    # Lando audio player
    lando_audio = fta.Audio(
        src="lando.mp3",
        autoplay=False,
        volume=1.0,
        release_mode=fta.ReleaseMode.STOP,
    )

    # Max Verstappen audio player
    max_audio_player = fta.Audio(
        src="Max_verstappen.mp3",
        autoplay=False,
        volume=1.0,
        release_mode=fta.ReleaseMode.STOP,
    )

    # Oscar Down Under audio player
    down_under_audio = fta.Audio(
        src="Down_under.mp3",
        autoplay=False,
        volume=1.0,
        release_mode=fta.ReleaseMode.STOP,
    )

    # Sebastian Vettel audio player
    vettel_audio = fta.Audio(
        src="Vettel.mp3",
        autoplay=False,
        volume=1.0,
        release_mode=fta.ReleaseMode.STOP,
    )

    # Isack Hadjar audio player
    isack_audio = fta.Audio(
        src="Isack_Hadjar.mp3",
        autoplay=False,
        volume=1.0,
        release_mode=fta.ReleaseMode.STOP,
    )

    # The Final Countdown audio player
    final_countdown_audio = fta.Audio(
        src="The_Final_Countdown.mp3",
        autoplay=False,
        volume=1.0,
        release_mode=fta.ReleaseMode.STOP,
    )

    # Star Wars audio player
    star_wars_audio = fta.Audio(
        src="Star_wars.mp3",
        autoplay=False,
        volume=1.0,
        release_mode=fta.ReleaseMode.STOP,
    )

    # Kimi audio player
    kimi_audio = fta.Audio(
        src="kimi.mp3",
        autoplay=False,
        volume=1.0,
        release_mode=fta.ReleaseMode.STOP,
    )

    page.services.append(lando_audio)
    page.services.append(max_audio_player)
    page.services.append(down_under_audio)
    page.services.append(vettel_audio)
    page.services.append(isack_audio)
    page.services.append(final_countdown_audio)
    page.services.append(star_wars_audio)
    page.services.append(kimi_audio)

    # Audio functions
    async def play_lando(e):
        await lando_audio.play()

    async def play_max(e):
        await max_audio_player.play()

    async def play_down_under(e):
        await down_under_audio.play()

    async def play_vettel(e):
        await vettel_audio.play()

    async def play_isack(e):
        await isack_audio.play()

    async def play_kimi(e):
        await kimi_audio.play()

    # Lando button
    lando_button = ft.Button(
        content=ft.Text(
            "▶ LANDO",
            color=ft.Colors.WHITE,
        ),
        bgcolor="#222222",
        visible=False,
        on_click=play_lando,
    )

    # Max button
    max_button = ft.Button(
        content=ft.Text(
            "▶ DU DU DU DU",
            color=ft.Colors.RED,
        ),
        bgcolor="#000000",
        visible=False,
        on_click=play_max,
    )

    # Down Under button
    down_under_button = ft.Button(
        content=ft.Text(
            "▶ DOWN UNDER",
            color=ft.Colors.WHITE,
        ),
        bgcolor="#00843D",
        visible=False,
        on_click=play_down_under,
    )

    # Vettel button
    vettel_button = ft.Button(
        content=ft.Text(
            "▶ SEB VETTEL",
            color=ft.Colors.RED,
        ),
        bgcolor="#000000",
        visible=False,
        on_click=play_vettel,
    )

    # Isack Hadjar button
    isack_button = ft.Button(
        content=ft.Text(
            "▶ ISACK HADJAR",
            color=ft.Colors.RED,
        ),
        bgcolor="#000000",
        visible=False,
        on_click=play_isack,
    )

    # Kimi button
    kimi_button = ft.Button(
        content=ft.Text(
            "▶ KIMI",
            color=ft.Colors.WHITE,
        ),
        bgcolor="#008080",
        visible=False,
        on_click=play_kimi,
    )

    # Button containers
    lando_button_container = ft.Container(
        content=lando_button,
        alignment=ft.Alignment.CENTER,
        padding=ft.Padding.only(top=120),
        expand=True,
        ignore_interactions=True,
    )

    max_button_container = ft.Container(
        content=max_button,
        alignment=ft.Alignment.CENTER,
        padding=ft.Padding.only(top=120),
        expand=True,
        ignore_interactions=True,
    )

    vettel_button_container = ft.Container(
        content=vettel_button,
        alignment=ft.Alignment.CENTER,
        padding=ft.Padding.only(top=120),
        expand=True,
        ignore_interactions=True,
    )

    isack_button_container = ft.Container(
        content=isack_button,
        alignment=ft.Alignment.CENTER,
        padding=ft.Padding.only(top=120),
        expand=True,
        ignore_interactions=True,
    )

    # Kimi button container
    kimi_button_container = ft.Container(
        content=kimi_button,
        alignment=ft.Alignment.CENTER,
        padding=ft.Padding.only(top=120),
        expand=True,
        ignore_interactions=True,
    )

    # Down Under button stays above number 81
    down_under_button_container = ft.Container(
        content=down_under_button,
        alignment=ft.Alignment.CENTER,
        padding=ft.Padding.only(bottom=140),
        expand=True,
        ignore_interactions=True,
    )

    # Normal counter click
    async def increment_click(e):

        # Stop music when moving to another number
        await down_under_audio.pause()
        await lando_audio.pause()
        await isack_audio.pause()
        await max_audio_player.pause()
        await star_wars_audio.pause()
        await final_countdown_audio.pause()
        await vettel_audio.pause()
        await kimi_audio.pause()

        if counter.data >= 10:
            counter.data = 0
        else:
            counter.data += 1

        counter.value = str(counter.data)

        # Play The Final Countdown when counter reaches 0
        if counter.data == 0:
            await final_countdown_audio.play()

        # Restore counter and hide credits when continuing
        counter.visible = True
        end_credits_text.visible = False

        easter_egg_text.visible = False
        down_under_button.visible = False

        if counter.data == 3:
            page.bgcolor = "#00008B"
            counter.color = "#DB1313"
            max_button.visible = True

        elif counter.data == 4:
            page.bgcolor = "#FF7431"
            counter.color = "#000000"
            lando_button.visible = True

        elif counter.data == 5:
            page.bgcolor = "#00008B"
            counter.color = "#EC0808"
            vettel_button.visible = True

        elif counter.data == 6:
            page.bgcolor = "#00008B"
            counter.color = "#EE0A0A"
            isack_button.visible = True

        else:
            page.bgcolor = "#FFFFFF"
            counter.color = "#000000"

        # Allow clicks only on the currently visible button
        lando_button_container.ignore_interactions = counter.data != 4
        max_button_container.ignore_interactions = counter.data != 3
        vettel_button_container.ignore_interactions = counter.data != 5
        isack_button_container.ignore_interactions = counter.data != 6

        # Hide other audio buttons
        if counter.data != 3:
            max_button.visible = False

        if counter.data != 4:
            lando_button.visible = False

        if counter.data != 5:
            vettel_button.visible = False

        if counter.data != 6:
            isack_button.visible = False

        # Hide Kimi button
        kimi_button.visible = False
        kimi_button_container.ignore_interactions = True

        down_under_button_container.ignore_interactions = True

        page.update()

    # Oscar Easter egg
    def secret_click(e):

        counter.data = 81
        counter.value = "81"

        counter.visible = True
        end_credits_text.visible = False

        page.bgcolor = "#FF7431"
        counter.color = "#000000"

        lando_button.visible = False
        max_button.visible = False
        vettel_button.visible = False
        isack_button.visible = False
        kimi_button.visible = False

        lando_button_container.ignore_interactions = True
        max_button_container.ignore_interactions = True
        vettel_button_container.ignore_interactions = True
        isack_button_container.ignore_interactions = True
        kimi_button_container.ignore_interactions = True

        easter_egg_text.visible = True
        down_under_button.visible = True

        down_under_button_container.ignore_interactions = False

        page.update()

    # Kimi Easter egg
    async def kimi_click(e):

        # Pause all other music
        await down_under_audio.pause()
        await lando_audio.pause()
        await isack_audio.pause()
        await max_audio_player.pause()
        await star_wars_audio.pause()
        await final_countdown_audio.pause()
        await vettel_audio.pause()
        await kimi_audio.pause()

        # Show number 12
        counter.data = 12
        counter.value = "12"
        counter.visible = True

        # Teal background and white number
        page.bgcolor = "#33C9C9"
        counter.color = "#FFFFFF"

        # Hide other screens
        end_credits_text.visible = False
        easter_egg_text.visible = False

        # Hide other buttons
        lando_button.visible = False
        max_button.visible = False
        vettel_button.visible = False
        isack_button.visible = False
        down_under_button.visible = False

        # Disable other button interactions
        lando_button_container.ignore_interactions = True
        max_button_container.ignore_interactions = True
        vettel_button_container.ignore_interactions = True
        isack_button_container.ignore_interactions = True
        down_under_button_container.ignore_interactions = True

        # Show Kimi button
        kimi_button.visible = True
        kimi_button_container.ignore_interactions = False

        page.update()

        # IMPORTANT: No automatic audio playback here.
        # The Kimi sound plays only when the Kimi button is pressed.

    # End credits long press
    async def credits_click(e):

        await down_under_audio.pause()
        await lando_audio.pause()
        await isack_audio.pause()
        await max_audio_player.pause()
        await vettel_audio.pause()
        await final_countdown_audio.pause()
        await kimi_audio.pause()

        await star_wars_audio.play()

        page.bgcolor = "#000000"

        counter.visible = False
        end_credits_text.visible = True

        easter_egg_text.visible = False
        down_under_button.visible = False

        lando_button.visible = False
        max_button.visible = False
        vettel_button.visible = False
        isack_button.visible = False
        kimi_button.visible = False

        lando_button_container.ignore_interactions = True
        max_button_container.ignore_interactions = True
        vettel_button_container.ignore_interactions = True
        isack_button_container.ignore_interactions = True
        kimi_button_container.ignore_interactions = True

        down_under_button_container.ignore_interactions = True

        page.update()

    # Floating button with long press for end credits
    page.floating_action_button = ft.GestureDetector(
        content=ft.FloatingActionButton(
            icon=ft.Icons.ADD,
            on_click=increment_click,
        ),
        on_long_press=credits_click,
    )

    # Physical keyboard F1 and CTRL + F2
    async def on_keyboard(e: ft.KeyboardEvent):

        if e.key == "F1":
            secret_click(e)

        elif e.key == "F2" and e.ctrl:
            await kimi_click(e)

    page.on_keyboard_event = on_keyboard

    # Main layout
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Stack(
                controls=[

                    # Counter stays centered
                    ft.Container(
                        content=counter,
                        alignment=ft.Alignment.CENTER,
                        expand=True,
                    ),

                    # Lando button
                    lando_button_container,

                    # Max button
                    max_button_container,

                    # Vettel button
                    vettel_button_container,

                    # Isack button
                    isack_button_container,

                    # Kimi button
                    kimi_button_container,

                    # Down Under button above Oscar's 81
                    down_under_button_container,

                    # Oscar message
                    ft.Container(
                        content=easter_egg_text,
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.only(top=180),
                        expand=True,
                        ignore_interactions=True,
                    ),

                    # End credits screen
                    ft.Container(
                        content=end_credits_text,
                        alignment=ft.Alignment.CENTER,
                        expand=True,
                        ignore_interactions=True,
                    ),

                ],
                expand=True,
            ),
        )
    )


ft.run(main, assets_dir="assets")