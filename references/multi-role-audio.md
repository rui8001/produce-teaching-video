# Multi-role continuous-audio gate

Use this only when the same speaker has non-contiguous lines.

1. Synthesize or record each speaker's complete set of lines in one continuous take. Do not synthesize each sentence and concatenate it.
2. Request a complete ending for every segment and clear silence between separated segments.
3. Verify the returned speech semantically before cutting.
4. Detect real silence locally. A boundary is usable only when it contains a continuous quiet region appropriate to the recording; use the midpoint of that region.
5. If any required boundary lacks verified silence, reject the whole speaker track for cutting. Re-record or regenerate the continuous role track with authorization.
6. Review every role switch for complete words, correct order, natural tails, energy, and timing. Global transcript similarity cannot clear a local cut defect.

Do not use a transcript word end, an ordinary waveform dip, or repeated trial-and-error cut movement as a substitute for verified silence.
