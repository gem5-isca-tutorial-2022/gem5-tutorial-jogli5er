from gem5.resources.resource import Resource

# You can implement a custom resource to specify where to download from if you have it e.g. in a repo
resource = Resource("riscv-disk-img")

print(f"The resource is available at {resource.get_local_path()}")

