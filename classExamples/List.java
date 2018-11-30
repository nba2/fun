// An implementation of a Python-like List class, in Java.
// (c) The great Class of Fall 2018

public class List
{
  private Object[] data;
  private int allocation;
  private int size;

  public List()
  {
    allocation = 12;
    size = 0;
    data = new Object[allocation];
  }

  public int size()
  {
    return size;
  }

  public Object get(int i)
  {
    return data[i];
  }

  public void set(int i, Object v)
  {
    data[i] = v;
  }

  private void ensureCapacity(int count)
  {
    if (count > allocation) {
      allocation = 2 * count;
      Object[] temp = new Object[allocation];
      for (int i = 0; i < size; i++) {
        temp[i] = data[i];
      }
      data = temp;
    }
  }

  public void append(Object v)
  {
    ensureCapacity(size + 1);
    data[size] = v;
    size = size++;
  }

  public Object pop(int i)
  {
    Object result = data[i];
    for (int loc = i; loc < (size - 1); i++) {
      data[loc] = data[loc + 1];
    }
    return result;
  }

  public Object pop()
  {
    return pop(size-1);
  }

}
