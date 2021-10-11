from Manjaro.CLI import color
import click
color.title()


@click.command()
@click.option("--install", "-i", metavar="Packages(s)", help="install native packages")
@click.option("--install-flatpaks", "-if", metavar="Packages(s)", help="install flatpaks")
@click.option("--install-snaps", "-is", metavar="Packages(s)", help="install snaps")
@click.option("--remove", "-r", metavar="Packages(s)", help="remove packages")
@click.option("--remove-flatpaks", "-rf", metavar="Packages(s)", help="remove flatpaks")
@click.option("--remove-snaps", "-rs", metavar="Packages(s)", help="remove snaps")
@click.option("--search", "-sp", metavar="Name(s)", help="search package")
@click.option("--search-flatpak", "-sf", metavar="Name(s)", help="search flatpak")
@click.option("--search-snap", "-ss", metavar="Name(s)", help="search snap")
@click.option("--search-all", "-sa", metavar="Name(s)", help="search all package formats")
@click.option("--refresh", "-ref", metavar="Options=( database )", help="Refresh keys/mirrors/database")
@click.option("--graphic-drivers", "-gd", metavar="Options=( -info/-set-open/-set-proprietary )", help="Information or detect and install graphic drivers")
@click.option("--branch", "-br", metavar="Options=( -info/-set-stable/-set-staging/-set-testing/-set-unstable )", help="search package")
@click.option("--journal", "-j", metavar="Options=( -error/-warning/-debug/-info )", help="Display messages in your system for debuging purposes")
def cli(
    install,
    install_flatpaks,
    install_snaps,
    remove,
    remove_flatpaks,
    remove_snaps,
    search,
    search_flatpak,
    search_snap,
    search_all,
    refresh,
    graphic_drivers,
    branch,
    journal
):
    if search_flatpak or search_snap or search or search_all:
        from Manjaro.CLI.packages import _check_plugin_support, Search_flatpaks, Search_pkgs, Search_snaps
        if search_all:
            _check_plugin_support(format="flatpak")
            _check_plugin_support(format="snap")
            Search_pkgs(search_all)
            Search_flatpaks(search_all)
            Search_snaps(search_all)

        elif search:
            Search_pkgs(search)

        elif search_flatpak:
            _check_plugin_support(format="flatpak")
            Search.flatpaks(search_flatpak)

        elif search_snap:
            _check_plugin_support(format="snap")
            Search_snaps(search_snap)

    if refresh:
        from Manjaro.CLI import Refresh
        Refresh.database(refresh)

    if branch:
        from Manjaro.CLI import Branch
        if branch == "-info":
            Branch.info()
        elif branch == "-set-stable":
            Branch.stable()

        elif branch == "-set-staging":
            Branch.staging()

        elif branch == "-set-testing":
            Branch.testing()

        elif branch == "-set-unstable":
            Branch.unstable()
        else:
            color.red("Syntax is ( manjaro --branch -set-stable )")

    if install or install_flatpaks or install_snaps \
            or remove or remove_flatpaks or remove_snaps:
        from Manjaro.CLI.packages import _check_plugin_support, pamac
        from Manjaro.CLI.packages import add_pkg, add_snaps, add_flatpaks
        from Manjaro.CLI.packages import uninstall_pkgs, uninstall_snaps, uninstall_flatpaks
        if install:
            add_pkg(install)

        if install_snaps:
            _check_plugin_support(format="snap")
            add_snaps(install_snaps)

        if install_flatpaks:
            _check_plugin_support(format="flatpak")
            add_flatpaks(install_flatpaks)         

        if remove:
            uninstall_pkgs(remove)

        if remove_flatpaks:
            _check_plugin_support(format="flatpak")
            uninstall_flatpaks(remove_flatpaks)

        if remove_snaps:
            _check_plugin_support(format="snap")
            uninstall_snaps(remove_snaps)

        pamac.run()

    if graphic_drivers:
        from Manjaro.SDK import Hardware
        if graphic_drivers == "-info":
            Hardware.Info().graphics_driver()

        elif graphic_drivers == "-set-open":
            Hardware.Graphics.set_open()

        elif graphic_drivers == "-set-proprietary":
            Hardware.Graphics.set_open()

    if journal:
        from Manjaro.CLI import Diagnose
        if journal == "-error":
            Diagnose.error()

        elif journal == "-debug":
            Diagnose.debug()

        elif journal == "-warning":
            Diagnose.warning()

        elif journal == "-info":
            Diagnose.info()

        else:
            color.red("Available options is [ -info/-error/-warning/-info ]")
