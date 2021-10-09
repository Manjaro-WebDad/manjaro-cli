from Manjaro.SDK import PackageManager
from Manjaro.CLI import color
pamac = PackageManager.Pamac()

def add_pkg(pkgs):
    color.action("Instaling and upgrading packages")
    _list = pkgs.split(" ")
    return pamac.add_pkgs_to_install(_list)


def add_flatpaks(pkgs):
    color.action("Instaling and upgrading flatpaks")
    _list = []
    for p in pkgs.split(" "):
        pkg_object = pamac.search_flatpaks(p)
        for pkg in pkg_object:
            if pkg.get_name() == p:
                _list.append(pkg)
    
    pamac.add_pkgs_to_install(_list, pkg_format="flatpaks")


def add_snaps(pkgs):
    color.action("Instaling and upgrading snaps")
    _list = []
    for p in pkgs.split(" "):
        pkg_object = pamac.search_snaps(p)
        for pkg in pkg_object:
            if pkg.get_name() == p:
                _list.append(pkg)

    pamac.add_pkgs_to_install(_list, pkg_format="snaps")


def uninstall_snaps(pkgs):
    color.action("Removing snaps")
    _list = []
    for p in pkgs.split(" "):
        pkg_object = pamac.search_snaps(p)
        for pkg in pkg_object:
            if pkg.get_name() == p:
                _list.append(pkg)

    pamac.add_pkgs_to_remove(_list, pkg_format="snaps")


def uninstall_flatpaks(pkgs):
    color.action("Removing flatpaks")
    _list = []
    for p in pkgs.split(" "):
        pkg_object = pamac.search_flatpaks(p)
        for pkg in pkg_object:
            if pkg.get_name() == p:
                _list.append(pkg)
    
    pamac.add_pkgs_to_remove(_list, pkg_format="flatpaks")


def uninstall_pkgs(pkgs):
    color.action("Removing packages")
    _list = pkgs.split(" ")
    pamac.add_pkgs_to_remove(_list)


def Search_pkgs(pkgs):
    color.action("Native Packages Search Results".upper())
    _list = pkgs.split(" ")
    for pkg in _list:
        p = pamac.search_pkgs(pkg)
        if p:
            for i in p:
                color.red(i.get_name())
                title = i.get_app_name()
                if title:
                    color.cyan(title)

                desc = i.get_desc()
                if desc:
                    color.white(desc)
        else:
            color.red("Not Found".upper())
        print()


def Search_snaps(snaps):
    color.action("Snaps Search Results".upper())
    _list = snaps.split(" ")
    for pkg in _list:
        p = pamac.search_snaps(snaps)
        if p:
            for i in p:
                color.red(i.get_name())
                title = i.get_app_name()
                if title:
                    color.cyan(title)

                desc = i.get_desc()
                if desc:
                    color.white(desc)
        else:
            color.red("Not Found")
        print()


def Search_flatpaks(flatpaks):
    color.action("Flatpak Search Results".upper())
    _list = flatpaks.split(" ")
    for pkg in _list:
        p = pamac.search_flatpaks(flatpaks)
        if p:
            for i in p:
                color.red(i.get_name())
                title = i.get_app_name()
                if title:
                    color.cyan(title)

                desc = i.get_desc()
                if desc:
                    color.white(desc)
        else:
            color.red("Not Found")
        print()