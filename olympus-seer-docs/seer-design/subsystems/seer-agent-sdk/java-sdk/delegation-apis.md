# Delegation APIs (Java)

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-17  
> **Related**: [Request-Scoped Delegation](../../../implementation-concepts/request-scoped-delegation.md)

---

## Overview

The Delegation APIs enable agents to work with request-scoped authority delegation. These APIs provide Java equivalents to the Python Delegation APIs with language-appropriate idioms.

---

## Core APIs

### HubClient Delegation Methods

```java
package com.olympus.seer.sdk.hub;

import com.olympus.seer.sdk.delegation.*;
import java.time.Duration;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.CompletableFuture;

public class HubClient {
    
    /**
     * Request delegation authority from the user.
     * 
     * This posts an AUTHORITY_REQUEST and waits for the response.
     * The Channel will prompt the user (or auto-fulfill from existing
     * certificates).
     *
     * @param templateId ID of the Delegation Template to request
     * @param reason Human-readable reason for the request
     * @param timeout How long to wait for user response
     * @return DelegationToken if granted
     * @throws AuthorityDeniedException User denied the request
     * @throws AuthorityTimeoutException Request timed out
     * @throws DelegationException Other delegation errors
     */
    public CompletableFuture<DelegationToken> requestAuthority(
            String templateId,
            String reason,
            Duration timeout) {
        // Implementation
    }
    
    /**
     * Request authority with default timeout (5 minutes).
     */
    public CompletableFuture<DelegationToken> requestAuthority(
            String templateId,
            String reason) {
        return requestAuthority(templateId, reason, Duration.ofMinutes(5));
    }
    
    /**
     * Get an available delegation token for the specified template.
     *
     * @param templateId ID of the Delegation Template
     * @return Optional containing token if available
     */
    public Optional<DelegationToken> getDelegationToken(String templateId) {
        // Implementation
    }
    
    /**
     * Get all available delegation tokens for this request.
     *
     * @return List of all DelegationToken objects
     */
    public List<DelegationToken> getAllDelegationTokens() {
        // Implementation
    }
    
    /**
     * Check if agent has delegation for the specified template.
     *
     * @param templateId ID of the Delegation Template
     * @return true if delegation is available
     */
    public boolean hasDelegation(String templateId) {
        return getDelegationToken(templateId).isPresent();
    }
    
    /**
     * Delegate authority to a child agent.
     *
     * @param childAgentId SPIFFE ID of the child agent
     * @param templateId Template to delegate
     * @return DelegationToken for the child agent
     * @throws ChainingNotAllowedException Token doesn't allow chaining
     * @throws DelegationException Other delegation errors
     */
    public CompletableFuture<DelegationToken> delegateToChild(
            String childAgentId,
            String templateId) {
        // Implementation
    }
    
    /**
     * Check if current token allows chaining to child agents.
     *
     * @param templateId Optional template ID to check specific token
     * @return true if chaining is allowed
     */
    public boolean canDelegateToChild(String templateId) {
        return getDelegationToken(templateId)
            .map(DelegationToken::isChainingAllowed)
            .orElse(false);
    }
}
```

---

## Data Classes

### DelegationToken

```java
package com.olympus.seer.sdk.delegation;

import java.time.Instant;
import java.util.List;
import java.util.Map;

public class DelegationToken {
    
    private final String token;
    private final String templateId;
    private final String delegatorId;
    private final Instant expiresAt;
    private final List<String> permissions;
    private final Map<String, Object> constraints;
    private final boolean chainingAllowed;
    
    // Constructor
    public DelegationToken(
            String token,
            String templateId,
            String delegatorId,
            Instant expiresAt,
            List<String> permissions,
            Map<String, Object> constraints,
            boolean chainingAllowed) {
        this.token = token;
        this.templateId = templateId;
        this.delegatorId = delegatorId;
        this.expiresAt = expiresAt;
        this.permissions = permissions;
        this.constraints = constraints;
        this.chainingAllowed = chainingAllowed;
    }
    
    // Getters
    public String getToken() { return token; }
    public String getTemplateId() { return templateId; }
    public String getDelegatorId() { return delegatorId; }
    public Instant getExpiresAt() { return expiresAt; }
    public List<String> getPermissions() { return permissions; }
    public Map<String, Object> getConstraints() { return constraints; }
    public boolean isChainingAllowed() { return chainingAllowed; }
    
    /**
     * Check if token is expired.
     */
    public boolean isExpired() {
        return Instant.now().isAfter(expiresAt);
    }
    
    /**
     * Get header map for API calls.
     */
    public Map<String, String> toHeader() {
        return Map.of("X-Delegation-Token", token);
    }
}
```

### AuthorityRequest

```java
package com.olympus.seer.sdk.delegation;

import java.time.Duration;

public class AuthorityRequest {
    
    private final String templateId;
    private final String reason;
    private final Duration timeout;
    
    public AuthorityRequest(String templateId, String reason) {
        this(templateId, reason, Duration.ofMinutes(5));
    }
    
    public AuthorityRequest(String templateId, String reason, Duration timeout) {
        this.templateId = templateId;
        this.reason = reason;
        this.timeout = timeout;
    }
    
    // Getters
    public String getTemplateId() { return templateId; }
    public String getReason() { return reason; }
    public Duration getTimeout() { return timeout; }
}
```

---

## Usage Examples

### Basic Authority Request

```java
import com.olympus.seer.sdk.hub.HubClient;
import com.olympus.seer.sdk.delegation.*;

public class PaymentProcessor {
    
    private final HubClient hubClient;
    
    public CompletableFuture<PaymentResult> processPayment(PaymentRequest request) {
        // Check if we already have authority
        if (!hubClient.hasDelegation("personal-finance-assistant")) {
            return hubClient.requestAuthority(
                    "personal-finance-assistant",
                    "Need to initiate payment on your behalf")
                .thenCompose(token -> {
                    // Authority granted, proceed with payment
                    return initiatePayment(request, token);
                })
                .exceptionally(ex -> {
                    if (ex.getCause() instanceof AuthorityDeniedException) {
                        // User denied - continue with degraded capability
                        return handleNoAuthority(request);
                    }
                    throw new RuntimeException(ex);
                });
        }
        
        // Already have authority
        DelegationToken token = hubClient.getDelegationToken("personal-finance-assistant")
            .orElseThrow();
        return initiatePayment(request, token);
    }
}
```

### Using Token with Tool Calls

```java
import com.olympus.seer.sdk.tools.ToolClient;

public class ToolInvoker {
    
    private final HubClient hubClient;
    private final ToolClient toolClient;
    
    public CompletableFuture<ToolResult> callPaymentTool(PaymentParams params) {
        DelegationToken token = hubClient.getDelegationToken("personal-finance-assistant")
            .orElseThrow(() -> new DelegationException("No delegation available"));
        
        // Token is passed to Tool Gateway
        return toolClient.call(
            "payment-initiate",
            params,
            token  // Delegation token
        );
    }
}
```

### Chaining to Child Agent

```java
public class ParentAgent {
    
    private final HubClient hubClient;
    private final ScenarioClient scenarioClient;
    
    public CompletableFuture<Void> delegateToChild() {
        if (!hubClient.canDelegateToChild("personal-finance-assistant")) {
            throw new ChainingNotAllowedException("Cannot delegate to child");
        }
        
        return hubClient.delegateToChild(
                "spiffe://seer/agents/child-payment-processor",
                "personal-finance-assistant")
            .thenCompose(childToken -> {
                // Pass to child via scenario invocation
                return scenarioClient.invoke(
                    "payment-processing",
                    List.of(childToken)
                );
            });
    }
}
```

### Graceful Degradation

```java
public class PortfolioViewer {
    
    public PortfolioView getPortfolioView() {
        Optional<DelegationToken> token = hubClient.getDelegationToken("view-investments");
        
        if (token.isPresent()) {
            // Full capability - show real portfolio
            Portfolio portfolio = fetchUserPortfolio(token.get());
            return formatPortfolio(portfolio);
        } else {
            // Degraded - show educational content
            return getEducationalContent("investment-basics");
        }
    }
}
```

---

## Exception Classes

```java
package com.olympus.seer.sdk.delegation;

public class DelegationException extends RuntimeException {
    public DelegationException(String message) {
        super(message);
    }
    
    public DelegationException(String message, Throwable cause) {
        super(message, cause);
    }
}

public class AuthorityDeniedException extends DelegationException {
    private final String denialReason;
    
    public AuthorityDeniedException(String reason) {
        super("Authority denied: " + reason);
        this.denialReason = reason;
    }
    
    public String getDenialReason() {
        return denialReason;
    }
}

public class AuthorityTimeoutException extends DelegationException {
    public AuthorityTimeoutException() {
        super("Authority request timed out");
    }
}

public class ChainingNotAllowedException extends DelegationException {
    public ChainingNotAllowedException(String message) {
        super(message);
    }
}

public class TokenExpiredException extends DelegationException {
    public TokenExpiredException() {
        super("Delegation token has expired");
    }
}

public class TokenRevokedException extends DelegationException {
    public TokenRevokedException() {
        super("Delegation token has been revoked");
    }
}
```

---

## Related Documentation

- [Hub Integration APIs](./hub-integration-apis.md) — Other Hub APIs
- [Python Delegation APIs](../python-sdk/delegation-apis.md) — Python equivalent
- [Request-Scoped Delegation](../../../implementation-concepts/request-scoped-delegation.md) — Comprehensive design

---

*Delegation APIs provide Java interfaces for request-scoped authority delegation.*
