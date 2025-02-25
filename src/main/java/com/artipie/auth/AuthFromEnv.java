/*
 * The MIT License (MIT) Copyright (c) 2020-2021 artipie.com
 * https://github.com/artipie/artipie/LICENSE.txt
 */
package com.artipie.auth;

import com.artipie.http.auth.Authentication;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;

/**
 * Authentication based on environment variables.
 * @since 0.3
 */
public final class AuthFromEnv implements Authentication {

    /**
     * Environment name for user.
     */
    public static final String ENV_NAME = "ARTIPIE_USER_NAME";

    /**
     * Environment name for password.
     */
    private static final String ENV_PASS = "ARTIPIE_USER_PASS";

    /**
     * Environment variables.
     */
    private final Map<String, String> env;

    /**
     * Default ctor with system environment.
     */
    public AuthFromEnv() {
        this(System.getenv());
    }

    /**
     * Primary ctor.
     * @param env Environment
     */
    public AuthFromEnv(final Map<String, String> env) {
        this.env = env;
    }

    @Override
    @SuppressWarnings("PMD.OnlyOneReturn")
    public Optional<Authentication.User> user(final String username, final String password) {
        final Optional<Authentication.User> result;
        // @checkstyle LineLengthCheck (5 lines)
        if (Objects.equals(Objects.requireNonNull(username), this.env.get(AuthFromEnv.ENV_NAME))
            && Objects.equals(Objects.requireNonNull(password), this.env.get(AuthFromEnv.ENV_PASS))) {
            result = Optional.of(new Authentication.User(username));
        } else {
            result = Optional.empty();
        }
        return result;
    }

    @Override
    public String toString() {
        return String.format("%s()", this.getClass().getSimpleName());
    }
}
