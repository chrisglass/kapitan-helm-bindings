from cffi import FFI

ffi = FFI()

# declare functions to export
ffi.cdef(
    """
    char* renderChart(char* p0, char* p1, char* p2, char* p3, char* p4, char* p5, char** p6, int p7);
    void free(void* ptr);
"""
)

ffi.set_source("kapitan_helm.helm_binding", None)  # specify name for importing this module

if __name__ == "__main__":
    ffi.compile(verbose=True)
