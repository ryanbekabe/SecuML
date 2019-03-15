# SecuML
# Copyright (C) 2016-2019  ANSSI
#
# SecuML is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# SecuML is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with SecuML. If not, see <http://www.gnu.org/licenses/>.

from secuml.core.projection.algos.lmnn import Lmnn
from . import SemiSupervisedProjectionConf


class LmnnConf(SemiSupervisedProjectionConf):

    def _get_algo(self):
        return Lmnn

    @staticmethod
    def from_json(obj, logger):
        return LmnnConf(logger, obj['num_components'], obj['multiclass'])

    @staticmethod
    def from_args(args, logger):
        return LmnnConf(logger, multiclass=args.multiclass)
