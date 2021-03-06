# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# Huawei self developed service from compute-ext

from openstack import service_filter


class EcsService(service_filter.ServiceFilter):
    """The ECS service."""

    valid_versions = [service_filter.ValidVersion('v1')]

    def __init__(self, version=None):
        """Create a compute service."""
        super(EcsService, self).__init__(service_type='ecs',
                                         requires_project_id=True,
                                         version=version)


class EcsServiceV1_1(service_filter.ServiceFilter):
    """The ECS ext service."""

    valid_versions = [service_filter.ValidVersion('v1')]

    def __init__(self, version=None):
        """Create a compute service."""
        super(EcsServiceV1_1, self).__init__(service_type='ecsv1.1',
                                             requires_project_id=True,
                                             version=version)
