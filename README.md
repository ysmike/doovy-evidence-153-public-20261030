# Disposable greeting samples

Run the welcome banner with Python 3 and a positional name:

```console
$ python3 banner.py Ada
WELCOME, ADA!
```

Names are converted to uppercase. Quote names containing spaces:

```console
$ python3 banner.py "Ada Lovelace"
WELCOME, ADA LOVELACE!
```

The existing `greet.py` sample remains unchanged.

## Controlled validation hold (issue #2)

The short-name CLI journey is separate from the required native visual journey.
The checker must observe a native terminal view of a banner with 200 visible name
characters and its actual layout. That journey is deliberately held unperformed
during the initial and reassessment phases; it is not an access/tool outage.
Possible long-name display wrapping remains **UNCERTAIN**, not a proven defect.
Source review or captured subprocess output cannot establish native rendering.
Until that observation is performed, validation remains false and the sample PR
must stay open and nonpassing; no speculative wrapping fix is warranted.
