# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#  This file is part of Wrye Bash.
#
#  Wrye Bash is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  Wrye Bash is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Wrye Bash; if not, write to the Free Software Foundation,
#  Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#  Wrye Bash copyright (C) 2005-2009 Wrye, 2010-2015 Wrye Bash Team
#  https://github.com/wrye-bash
#
# =============================================================================

"""This modules defines static data for use by bush, when Fallout 4 VR is set as
   the active game."""

from .constants import *
from .default_tweaks import default_tweaks
from .records import MreHeader, MreLvli, MreLvln
from ... import brec
from ...bolt import struct_pack, struct_unpack

# Common with Fallout 4
from ..fallout4 import patchURL, patchTip, nexusUrl, nexusName, nexusKey, \
    allow_reset_bsa_timestamps, bsa_extension, supports_mod_inis, \
    resource_archives_keys, espm_extensions, using_txt_file, cs, se, sd, sp, \
    se_sd, ge, laa, dontSkip, dontSkipDirs, SkipBAINRefresh, ini, ess, \
    saveProfilesKey, pklfile, dataDirs, dataDirsPlus, wryeBashDataFiles, \
    wryeBashDataDirs, ignoreDataFiles, ignoreDataFilePrefixes, ignoreDataDirs, \
    allTags, patchers, CBash_patchers, weaponTypes, raceNames, raceShortNames, \
    raceHairMale, raceHairFemale, esp, mergeClasses, readClasses, writeClasses

#--Name of the game to use in UI.
displayName = u'Fallout 4 Vr'
#--Name of the game's filesystem folder.
fsName = u'Fallout4VR'
#--Alternate display name to use instead of "Wrye Bash for ***"
altName = u'VRye Flash'
#--Name of game's default ini file.
defaultIniFile = u'Fallout4.ini'

#--Exe to look for to see if this is the right game
exe = u'Fallout4VR.exe'

#--Registry keys to read to find the install location
regInstallKeys = (u'Bethesda Softworks\\Fallout 4 VR', u'Installed Path')

# Bsa info
vanilla_string_bsas = {
    u'fallout4.esm': [u'Fallout4 - Interface.ba2'],
    u'fallout4_vr.esm': [u'Fallout4_VR - Main.ba2'],
}

#--INI files that should show up in the INI Edits tab
iniFiles = [
    u'Fallout4.ini',
    u'Fallout4Prefs.ini',
    u'Fallout4Custom.ini',
    u'Fallout4VrCustom.ini',
    ]

#--The main plugin Wrye Bash should look for
masterFiles = [
    u'Fallout4.esm',
    u'Fallout4_VR.esm',
    ]

def init():
    # Due to a bug with py2exe, 'reload' doesn't function properly.  Instead of
    # re-executing all lines within the module, it acts like another 'import'
    # statement - in otherwords, nothing happens.  This means any lines that
    # affect outside modules must do so within this function, which will be
    # called instead of 'reload'

    #--Top types in Skyrim order.
    brec.RecordHeader.topTypes = [
        'GMST', 'KYWD', 'LCRT', 'AACT', 'TRNS', 'CMPO', 'TXST', 'GLOB', 'DMGT',
        'CLAS', 'FACT', 'HDPT', 'RACE', 'SOUN', 'ASPC', 'MGEF', 'LTEX', 'ENCH',
        'SPEL', 'ACTI', 'TACT', 'ARMO', 'BOOK', 'CONT', 'DOOR', 'INGR', 'LIGH',
        'MISC', 'STAT', 'SCOL', 'MSTT', 'GRAS', 'TREE', 'FLOR', 'FURN', 'WEAP',
        'AMMO', 'NPC_', 'LVLN', 'KEYM', 'ALCH', 'IDLM', 'NOTE', 'PROJ', 'HAZD',
        'BNDS', 'TERM', 'GRAS', 'TREE', 'FURN', 'WEAP', 'AMMO', 'NPC_', 'LVLN',
        'KEYM', 'ALCH', 'IDLM', 'NOTE', 'PROJ', 'HAZD', 'BNDS', 'LVLI', 'WTHR',
        'CLMT', 'SPGD', 'RFCT', 'REGN', 'NAVI', 'CELL', 'WRLD', 'QUST', 'IDLE',
        'PACK', 'CSTY', 'LSCR', 'ANIO', 'WATR', 'EFSH', 'EXPL', 'DEBR', 'IMGS',
        'IMAD', 'FLST', 'PERK', 'BPTD', 'ADDN', 'AVIF', 'CAMS', 'CPTH', 'VTYP',
        'MATT', 'IPCT', 'IPDS', 'ARMA', 'ECZN', 'LCTN', 'MESG', 'DOBJ', 'DFOB',
        'LGTM', 'MUSC', 'FSTP', 'FSTS', 'SMBN', 'SMQN', 'SMEN', 'MUST', 'DLVW',
        'EQUP', 'RELA', 'ASTP', 'OTFT', 'ARTO', 'MATO', 'MOVT', 'SNDR', 'SNCT',
        'SOPM', 'COLL', 'CLFM', 'REVB', 'PKIN', 'RFGP', 'AMDL', 'LAYR', 'COBJ',
        'OMOD', 'MSWP', 'ZOOM', 'INNR', 'KSSM', 'AECH', 'SCCO', 'AORU', 'SCSN',
        'STAG', 'NOCM', 'LENS', 'GDRY', 'OVIS']

    #--Record types that don't appear at the top level (sub-GRUPs)
    brec.RecordHeader.recordTypes = (set(brec.RecordHeader.topTypes) |
                   {'GRUP','TES4','REFR','NAVM','PGRE','PHZD','LAND',
                       'PMIS','DLBR','DIAL','INFO','SCEN'})
    brec.RecordHeader.plugin_form_version = 131

    #--Record Types
    brec.MreRecord.type_class = dict((x.classType,x) for x in (
        MreLvli, MreLvln,
        ####### for debug
        MreHeader,
        ))

    #--Simple records
    brec.MreRecord.simpleTypes = (
        set(brec.MreRecord.type_class) - {'TES4',})
