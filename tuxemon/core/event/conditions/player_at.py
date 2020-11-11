#
# Tuxemon
# Copyright (c) 2014-2017 William Edwards <shadowapex@gmail.com>,
#                         Benjamin Bean <superman2k5@gmail.com>
#
# This file is part of Tuxemon
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from tuxemon.core.event.eventcondition import EventCondition


class PlayerAtCondition(EventCondition):
    """ Checks to see if an npc is at a current position on the map.
    """
    name = "player_at"

    def test(self, session, event, condition):
        """ Checks to see if the player is at a current position on the map.
        :param event:
        """
        player = session.player

        # Get the condition's rectangle area. If we're on a tile in that area, then this condition
        # should return True.
        area_x = range(event.rect.left, event.rect.right)
        area_y = range(event.rect.top, event.rect.bottom)

        # If the player is at the coordinates and the operator is set to true then return true
        if round(player.tile_pos[0]) in area_x and round(player.tile_pos[1]) in area_y:
            return True

        # If the player is at the coordinates and the operator is set to false then return false
        else:
            return False
