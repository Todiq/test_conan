# syntax = docker/dockerfile:1.2

FROM rockylinux:8.7-minimal

ARG USER="test"
ARG GROUP="${USER}"
ARG UID="1000"
ARG GID="1000"

ENV TEST_HOME="/home/${USER}"
ENV PATH="${TEST_HOME}/.local/bin:${PATH}"

WORKDIR "${TEST_HOME}"

COPY --chown="${USER}" Conan/ Test ./

RUN microdnf install --assumeyes \
	python3.9 \
	python39-devel \
	util-linux \
	gcc \
	gcc-c++ \
	make \
	nano \
	sudo \
	which \
	passwd \
	&& microdnf clean all \
	&& groupadd --system --gid "${GID}" "${GROUP}" \
	&& useradd --no-log-init --system --uid "${UID}" --gid "${GID}" --shell /bin/bash --create-home "${USER}" \
	&& usermod --append --groups wheel "${USER}" \
	&& passwd --delete "${USER}" \
	&& chown --recursive "${UID}":0 "${TEST_HOME}" \
	&& chmod --recursive g=u "${TEST_HOME}"

USER "${USER}"

RUN python3 -m pip --quiet install --upgrade pip cmake conan numpy virtualenv --user --no-warn-script-location --no-cache-dir \
	&& conan config install profile --target-folder profiles \
	&& mv "${HOME}/.conan2/profiles/profile" "${HOME}/.conan2/profiles/default" \
	&& conan install -verror . --build=missing \
	&& conan editable add alpha/ \
	&& conan build -verror alpha/ --build="missing" \
	&& rm -rf *.sh conanfile* profile

CMD [ "bash" ]