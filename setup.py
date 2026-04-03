from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup, Extension

# Dijkstra module
dijkstra_ext = Pybind11Extension(
    "dijkstra_graph",
    sources=[
        "cpp/graphs/dijkstra.cpp",
        "cpp/graphs/binding.cpp"
    ],
    include_dirs=["cpp"],
    cxx_std=17,
)

# Trie module
trie_ext = Pybind11Extension(
    "medicine_trie", 
    sources=[
        "cpp/trie/medicine_trie.cpp",
        "cpp/trie/binding.cpp"
    ],
    include_dirs=["cpp"],
    cxx_std=17,
)

setup(
    name="medilocate_cpp_modules",
    ext_modules=[dijkstra_ext, trie_ext],
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)
